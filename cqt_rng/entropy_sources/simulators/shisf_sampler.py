from ...base.entropy_source import EntropySource
from ...utils.constants import shi_unitary5

import strawberryfields as sf
from strawberryfields import ops
import numpy as np

class ShiSFSampler(EntropySource):
    def __init__(self, **kwargs):
        
        self.nb_modes = kwargs.get("nb_modes")
        self.unitary = kwargs.get("unitary")

        if self.nb_modes is None:
            self.nb_modes = 6

        if self.nb_modes % 2 or self.nb_modes <= 4:
            raise ValueError("Wrong number of modes (nb_modes) expected to be even and higher than 4!")
        

        if self.unitary is None and self.nb_modes == 10:
            self.unitary = shi_unitary5
        
        elif 2 * np.shape(self.unitary)[0] != self.nb_modes:
            raise ValueError(f"Wrong unitary dimensions expect to be ({int(self.nb_modes / 2)},{int(self.nb_modes / 2)})!")
        else:
            raise ValueError("No unitary given!")
        
        self.dep_seq_len = self.nb_modes * 2
        self.seq_len = self.nb_modes * 2
        

    def _successful_entanglement(self, sample):
        nb_modes = np.size(sample)
        return np.sum(sample[:nb_modes // 2]) == 1 and np.sum(sample[nb_modes // 2:]) == 1

    def _sf_simulator(self):

        eng = sf.Engine("fock", backend_options={"cutoff_dim": 3})
        prog = sf.Program(self.nb_modes)


        mid_l = int(np.floor(self.nb_modes / 2) - 1)
        mid_h = int(np.floor(self.nb_modes / 2))

        with prog.context as q:
            # Two-photons entanglement source
            ops.Fock(1) | q[mid_l]
            ops.Fock(1) | q[mid_h]

            ops.BSgate(phi = np.pi / 2) | (q[mid_l - 1], q[mid_l])
            ops.BSgate(phi = np.pi / 2) | (q[mid_h], q[mid_h + 1])

            ops.BSgate(theta = np.pi / 2, phi = np.pi / 2) | (q[mid_l], q[mid_h]) # SWAP

            # Interferometer
            ops.Interferometer(self.unitary) | q[:mid_l + 1]
            ops.Interferometer(self.unitary) | q[mid_h:][::-1]

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
        shots = int(np.ceil(length / self.seq_len))
        ret = np.array()
        for _ in range(shots):
            ret = np.append(ret, self._run_experiment())

        return np.copy(ret[:length]).astype(np.int8)