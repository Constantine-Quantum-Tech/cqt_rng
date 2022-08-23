from ..base.post_processor import PostProcessor
import numpy as np


class NoPostProcess(PostProcessor):
    def __init__(self):
        pass

    def postprocess(self, sample_1, sample_2):
        output = np.copy(np.append(sample_1, sample_2)).astype(np.int8)

        return output
