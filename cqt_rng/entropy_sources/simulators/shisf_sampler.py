from ...base.entropy_source import EntropySource
from ...utils.generate_haar_unitary import generate_haar_unitary

import strawberryfields as sf
from strawberryfields import ops
import numpy as np


class ShiSFSampler(EntropySource):
    """Simulates the Shi. and al. experiment on Strawberry Fields.

    Parameters:
        nb_modes (int, optional): Number of modes of the interferometer (should be an even number). Default to `6`.
        unitary_top (np.ndarray, optional): The unitary to apply on the top-half of the modes. Default to randomly generated haar matrix.
        unitary_bottom (np.ndarray, optional): The unitary to apply on the bottom-half of the modes. Default to randomly generated haar matrix.

    """

    def __init__(self, **kwargs):
        self.name = "ShiSFSampler"
        self.nb_modes = kwargs.get("nb_modes")
        self.unitary_top = kwargs.get("unitary_top")
        self.unitary_bottom = kwargs.get("unitary_bottom")

        if self.nb_modes is None:
            self.nb_modes = 6

        if self.nb_modes % 2 or self.nb_modes < 4:
            raise ValueError(
                "Wrong number of modes (nb_modes) expected to be even and higher than 3!"
            )

        if self.unitary_top is None:
            self.unitary_top = generate_haar_unitary(self.nb_modes // 2)

        if self.unitary_bottom is None:
            self.unitary_bottom = generate_haar_unitary(self.nb_modes // 2)

        if (
            np.shape(self.unitary_top)[0] != self.nb_modes // 2
            or np.shape(self.unitary_bottom)[0] != self.nb_modes // 2
            or np.shape(self.unitary_top)[1] != self.nb_modes // 2
            or np.shape(self.unitary_bottom)[1] != self.nb_modes // 2
        ):
            raise ValueError(
                f"Wrong unitary dimensions expect to be ({int(self.nb_modes / 2)},{int(self.nb_modes / 2)}) for top and bottom!"
            )

        self.dep_seq_len = self.nb_modes
        self.seq_len = self.nb_modes

    def _successful_entanglement(self, sample):
        nb_modes = np.size(sample)
        return (
            np.sum(sample[: nb_modes // 2]) == 1
            and np.sum(sample[nb_modes // 2 :]) == 1
        )

    def _sf_simulator(self):

        eng = sf.Engine("fock", backend_options={"cutoff_dim": 3})
        prog = sf.Program(self.nb_modes)

        mid_l = int(np.floor(self.nb_modes / 2) - 1)
        mid_h = int(np.floor(self.nb_modes / 2))

        with prog.context as q:
            # Two-photons entanglement source
            ops.Fock(1) | q[mid_l]
            ops.Fock(1) | q[mid_h]

            ops.BSgate(phi=np.pi / 2) | (q[mid_l - 1], q[mid_l])
            ops.BSgate(phi=np.pi / 2) | (q[mid_h], q[mid_h + 1])

            ops.BSgate(theta=np.pi / 2, phi=np.pi / 2) | (q[mid_l], q[mid_h])  # SWAP

            # Interferometer
            ops.Interferometer(self.unitary_top) | q[: mid_l + 1]
            ops.Interferometer(self.unitary_bottom) | q[mid_h:]

            # Detection
            ops.MeasureFock() | q

        sample = eng.run(prog).samples[0]
        return sample

    def _run_experiment(self):
        ran_once = False
        while not ran_once or self._successful_entanglement(sample):
            sample = self._sf_simulator()
            ran_once = True
        return sample

    def sample(self, length):
        shots = length // self.seq_len
        ret = np.array([])
        for _ in range(shots):
            ret = np.append(ret, self._run_experiment())

        return np.copy(ret[:length]).astype(np.int8)
