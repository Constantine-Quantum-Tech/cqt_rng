from ...base.entropy_source import EntropySource
from ...utils.utils import generate_output_states, get_subm_idx
from ...utils.constants import shi_unitary5, shi_input_dict
import numpy as np
from thewalrus import perm

from scipy.special import factorial
from collections import OrderedDict

class BosonSampler(EntropySource):
    
    def __init__(self, **kwargs):
        self.unitary = kwargs.get("unitary")
        self.input_dict = kwargs.get("input_dict")

        if self.unitary is None and self.input_dict is None:
            # self.unitary = block_diag(shi_unitary5[:, ::-1], shi_unitary5)
            self.unitary = shi_unitary5
            self.input_dict = shi_input_dict
        elif self.unitary is None or self.input_dict is None:
            raise ValueError("No unitary or input_dict given")
        else:
            self.input_dict = OrderedDict(self.input_dict)
        
        for k in self.input_dict.keys():
            if len(k) != np.shape(self.unitary)[0] or  len(k) != np.shape(self.unitary)[1]:
                raise ValueError("Incompatible input and unitary!")

        self.probs_ = BosonSampler.get_theo_prob(self.input_dict, self.unitary)
        for k in self.probs_.keys(): # fixing small prob errors
            if np.isclose(sum(self.probs_[k][1]), 1):
                self.probs_[k][1][0] = 1 - sum(self.probs_[k][1]) + self.probs_[k][1][0]

        self.dep_seq_len = len(list(self.input_dict.keys())[0])
        self.seq_len = len(list(self.input_dict.keys())[0])

    @staticmethod
    def get_theo_prob(input_dict, unitary):
        input_states = list(input_dict.keys())
        dim = np.shape(unitary)[0]
        output = dict()

        for inp_state_str in input_states:
            inp_state_array = np.array(list(inp_state_str)).astype(int)
            
            if len(inp_state_str) != dim:
                raise Exception("Uncompatible input state and unitary!")

            total_photons = np.sum(inp_state_array)
            output_states = generate_output_states(total_photons, dim)

            for out_state_str in output_states:
                out_state_array = np.array(list(out_state_str)).astype(int)
                
                denum = np.prod(factorial(inp_state_array)) * np.prod(factorial(out_state_array)) 

                inp_idx = get_subm_idx(inp_state_array)
                out_idx = get_subm_idx(out_state_array)

                subm = unitary[:, inp_idx][out_idx]

                theo_prob = np.abs(perm(subm))**2 / denum
                global_theo_prob = theo_prob * input_dict[inp_state_str]
                if output.get(inp_state_str) is None:
                    output[inp_state_str] = [[out_state_str], [theo_prob], [global_theo_prob]]
                else:
                    output[inp_state_str][0].append(out_state_str)
                    output[inp_state_str][1].append(theo_prob)
                    output[inp_state_str][2].append(global_theo_prob)

        return output



    def _simulate(self, shots):
        entangled_state = np.random.choice(list(self.input_dict.keys()), p=list(self.input_dict.values()), size=shots) 

        res = []
        for es in entangled_state:
            output = np.random.choice(self.probs_[es][0], p = self.probs_[es][1])
            bs = [int(o) for o in output]
            res.extend(bs)
        return np.array(res)

    def sample(self, length):
        shots = int(np.ceil(length / self.seq_len))
        return np.copy(self._simulate(shots)[:length]).astype(np.int8)