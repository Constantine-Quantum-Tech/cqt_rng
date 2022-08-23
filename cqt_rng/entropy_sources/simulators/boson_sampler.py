from ...base.entropy_source import EntropySource
from ...utils.utils import generate_output_states, get_subm_idx
from ...utils.generate_haar_unitary import generate_haar_unitary
import numpy as np
from thewalrus import perm

from scipy.linalg import block_diag
from scipy.special import factorial
from collections import OrderedDict


class BosonSampler(EntropySource):
    """A boson sampling simulator.

    Parameters:
        unitary (np.ndarray, optional): the (n, n) interferometer matrix. Defaults to Shi et al.
         type matrix.
        input_dict (dict[str, float], optional): a dictionnary where the keys are string
        which represents the number of photons in each mode. And the values
        are the probabilities for each input. Default to a Shi et al. input.

    Examples:
        To simulate sending 1 photon in the first mode, 2 in the second
        mode, 3 in the third mode through a 3 mode interferometer::

            input_dict = {"123": 1}

        To simulate sending either a photon in the first mode or a photon in the second
        mode with 50% probability each a 2 mode interferometer::

            input_dict = {"10": 0.5, "01": 0.5}
    """

    def __init__(self, **kwargs):
        self.name = "BosonSampler"
        self.unitary = kwargs.get("unitary")
        self.input_dict = kwargs.get("input_dict")

        if self.unitary is None and self.input_dict is None:
            self.unitary = block_diag(
                generate_haar_unitary(5), generate_haar_unitary(5)
            )
            self.input_dict = {"0001100000": 0.5, "0000011000": 0.5}
        elif self.unitary is None or self.unitary is None:
            raise Exception("Unitary and input_dict needed!")
        else:
            self.input_dict = OrderedDict(self.input_dict)

        for k in self.input_dict.keys():
            if (
                len(k) != np.shape(self.unitary)[0]
                or len(k) != np.shape(self.unitary)[1]
            ):
                raise ValueError("Incompatible input and unitary!")

        self.probs_ = BosonSampler.get_theo_prob(self.input_dict, self.unitary)

        for k in self.probs_.keys():  # fixing small prob errors
            if np.isclose(sum(self.probs_[k][1]), 1):
                self.probs_[k][1][0] = 1 - sum(self.probs_[k][1]) + self.probs_[k][1][0]

        self.dep_seq_len = len(list(self.input_dict.keys())[0])
        self.seq_len = len(list(self.input_dict.keys())[0])

    @staticmethod
    def get_theo_prob(input_dict, unitary):
        """Takes an input_dict and a unitary and output the probabilities of the sampling outcome.

        Returns:
            dict([str, [[str], [float], [float]]]): a dictionnary where the keys are the same as the input keys. The values are a list of three lists.
            The first list lists all the possible outcomes. The second list gives the probability
            for each outcomes given that the initial state is guaranteed to be in the key state.
            The third list gives the probabilities of each outcome.

        """
        input_states = list(input_dict.keys())
        dim = np.shape(unitary)[0]
        output = dict()

        for inp_state_str in input_states:
            inp_state_array = np.array(list(inp_state_str)).astype(int)

            if len(inp_state_str) != dim:
                raise Exception("Uncompatible input state and unitary!")

            total_photons = np.sum(inp_state_array)
            output_states = generate_output_states(total_photons, dim)
            output_probs = np.zeros(len(output_states))
            output_global_probs = np.zeros(len(output_states))
            for i, out_state_str in enumerate(output_states):
                out_state_array = np.array(list(out_state_str)).astype(int)

                denum = np.prod(factorial(inp_state_array)) * np.prod(
                    factorial(out_state_array)
                )

                inp_idx = get_subm_idx(inp_state_array)
                out_idx = get_subm_idx(out_state_array)

                subm = unitary[:, inp_idx][out_idx]

                theo_prob = np.abs(perm(subm)) ** 2 / denum
                global_theo_prob = theo_prob * input_dict[inp_state_str]
                output_probs[i] = theo_prob
                output_global_probs[i] = global_theo_prob
                if output.get(inp_state_str) is None:
                    output[inp_state_str] = [
                        output_states,
                        output_probs,
                        output_global_probs,
                    ]
        return output

    def _simulate(self, shots):
        entangled_state = np.random.choice(
            list(self.input_dict.keys()), p=list(self.input_dict.values()), size=shots
        )

        res = []
        for es in entangled_state:
            output = np.random.choice(
                self.probs_[es][0],
                p=np.where(self.probs_[es][1] < 0, 0, self.probs_[es][1]),
            )
            bs = [int(o) for o in output]
            res.extend(bs)
        return np.array(res)

    def sample(self, length):
        shots = int(np.ceil(length / self.seq_len))
        return np.copy(self._simulate(shots)[:length]).astype(np.int8)
