from ..base.entropy_source import EntropySource
import numpy as np


class Loader(EntropySource):
    """Loads data from the input and outputs it as sample.

    Parameters:
        data (np.ndarray): the data.
        is_string (bool, optional): whether the input is a string. Defaults to `False`.
        seq_len (int, optional): the length of the sequences. Defaults to `1`.
        dep_seq_len (int, optional): the length of the dependent subsequences. Default to `1`.

    """

    def __init__(self, **kwargs):
        self.name = "Loader"
        self.__data = kwargs.get("data")
        self.__is_string = kwargs.get("is_string")
        self.dep_seq_len = kwargs.get("dep_seq_len")
        self.seq_len = kwargs.get("seq_len")

        self.__curr_idx = 0

        if self.__data is None:
            raise ValueError("No data to load!")
        if self.__is_string is None:
            self.__is_string = False

        if self.dep_seq_len is None:
            self.dep_seq_len = 1

        if self.seq_len is None:
            self.seq_len = 1

        if self.__is_string:
            ret = []
            for item in self.__data:
                ret.extend([int(s) for s in item])
            self.data = np.array(ret).astype(np.int8)

    def sample(self, length):
        if len(self.__data) < self.__curr_idx + length:
            raise Exception("Ran out data!")
        ret = np.copy(self.__data[self.__curr_idx : self.__curr_idx + length])
        self.__curr_idx += length
        return ret.astype(np.int8)
