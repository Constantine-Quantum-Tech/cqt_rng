from ...base.entropy_source import EntropySource
import strawberryfields as sf
from strawberryfields.tdm import borealis_gbs, get_mode_indices
from strawberryfields.ops import Sgate, Rgate, BSgate, MeasureFock
import numpy as np


class BorealisSampler(EntropySource):
    """Sample taken from Borealis."""

    def __init__(self, **kwargs):
        self.dep_seq_len = 216
        self.seq_len = 216
        self.name = "BorealisSampler"

    def sample(self, length):
        shots = np.max([2 * length, 2])

        eng = sf.RemoteEngine("borealis")
        device = eng.device
        gate_args_list = borealis_gbs(device, modes=216, squeezing="high")
        delays = [1, 6, 36]
        n, N = get_mode_indices(delays)
        prog = sf.TDMProgram(N)

        with prog.context(*gate_args_list) as (p, q):
            Sgate(p[0]) | q[n[0]]
            for i in range(len(delays)):
                Rgate(p[2 * i + 1]) | q[n[i]]
                BSgate(p[2 * i + 2], np.pi / 2) | (q[n[i + 1]], q[n[i]])
            MeasureFock() | q[0]

        results = eng.run(prog, shots=shots, crop=True)
        samples = results.samples
        return np.ravel(samples)
