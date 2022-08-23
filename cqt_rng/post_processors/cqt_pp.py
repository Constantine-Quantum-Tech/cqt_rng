from ..base.post_processor import PostProcessor
from .von_neumann_pp import VonNeumannPP
import numpy as np


class CQTPP(PostProcessor):
    """Implementation of the CQTPP

    Parameters:
        dep_seq_len (int): The length of the dependent sequences.
    """

    def __init__(self, **kwargs):
        self.__dep_seq_len = kwargs.get("dep_seq_len")
        if self.__dep_seq_len is None:
            self.__dep_seq_len = 1

    def postprocess(self, sample_1, sample_2):
        ouput = np.array([], dtype=np.int8)
        for i in range(len(sample_1) // self.__dep_seq_len):
            sub_s1 = sample_1[i * self.__dep_seq_len : (i + 1) * self.__dep_seq_len]
            sub_s2 = sample_2[i * self.__dep_seq_len : (i + 1) * self.__dep_seq_len]
            postprocess_output = VonNeumannPP().postprocess(sub_s1, sub_s2)
            if np.size(postprocess_output):
                ouput = np.append(ouput, np.array([postprocess_output[0]]))
        return ouput
