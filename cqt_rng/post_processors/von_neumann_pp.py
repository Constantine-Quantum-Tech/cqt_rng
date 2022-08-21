from ..base.post_processor import PostProcessor
import numpy as np


class VonNeumannPP(PostProcessor):
    def __init__(self):
        pass

    def postprocess(self, sample_1, sample_2):
        bits_1 = np.ravel(np.array(sample_1) == 0).astype(np.int8)
        bits_2 = np.ravel(np.array(sample_2) == 0).astype(np.int8)

        arr = np.where(bits_1 > bits_2, np.zeros_like(bits_1), np.ones_like(bits_1))
        arr = np.where(bits_1 == bits_2, np.nan * np.ones_like(bits_1), arr)

        return arr[~np.isnan(arr)].astype(np.int8)
