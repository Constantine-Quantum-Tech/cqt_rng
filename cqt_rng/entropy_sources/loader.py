from ..base.entropy_source import EntropySource
import numpy as np

class Loader(EntropySource):
    def __init__(self, **kwargs):
        self.dep_seq_len = kwargs.get("dep_seq_len")
        self.seq_len = kwargs.get("seq_len")
        self._file = kwargs.get("file")
        self.data = kwargs.get("data")
        self.type = kwargs.get("dtype")
        self._curr_idx = 0

        if self._file is None and self.data is None:
            raise ValueError("No file or data to load!")

        if self.dep_seq_len is None:
            self.dep_seq_len = 1

        if self.seq_len is None:
            self.seq_len = 1

        if self.data is None:
            data = np.ravel(np.load(self._file))
            ret = []
            if self.type == "str":
                for item in data:
                    ret.extend([int(s) for s in item])
                self.data =  np.array(ret).astype(np.int8)
            else:
                self.data = data
        else:
            data = np.copy(self.data)
            if self.type == "str":
                for item in data:
                    ret.extend([int(s) for s in item])
                self.data =  np.array(ret).astype(np.int8)


        
        
    def sample(self, length):
        if len(self.data) < self._curr_idx + length:
            raise Exception("Ran out data!")
        ret = np.copy(self.data[self._curr_idx:self._curr_idx + length])
        self._curr_idx += length
        return ret.astype(np.int8)


