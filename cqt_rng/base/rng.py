import numpy as np
from tqdm import tqdm

class RNG():
    """
    TODO
    """

    def __init__(self, entropy_source, postprocessor):
        """
        TODO
        """
        self.entropy_source = entropy_source
        self.postprocessor = postprocessor

    def generate(self, length = 1024, unbiased = False):
        """
        TODO
        """
        dep_seq_len = self.entropy_source.dep_seq_len
        seq_len = self.entropy_source.seq_len
        bitstring = np.array([], dtype=np.int8)
        with tqdm(total=length) as pbar:
            while len(bitstring) < length:
                missing_length = length - len(bitstring)
                
                gen_len = (missing_length + (seq_len - (missing_length % seq_len)))

                sample_1 = self.entropy_source.sample(gen_len)
                sample_2 = self.entropy_source.sample(gen_len)
                new_bitstring = self.postprocessor.postprocess(sample_1, sample_2)
                bitstring = np.append(bitstring, new_bitstring)
                pbar.update(len(new_bitstring))

        return np.copy(bitstring[:length]).astype(np.int8)

