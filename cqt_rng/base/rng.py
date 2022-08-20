import numpy as np
from tqdm import tqdm

class RNG():
    """
    TODO
    """

    def __init__(self, entropy_source):
        """
        TODO
        """
        self.entropy_source = entropy_source
    @staticmethod
    def postprocess(sample_1, sample_2):
        """
            TODO: Von-Neumann post-processing
        """
        bits_1 = np.ravel(np.array(sample_1) == 0).astype(np.int8)
        bits_2 = np.ravel(np.array(sample_2) == 0).astype(np.int8)

        arr = np.where(bits_1 > bits_2, np.zeros_like(bits_1), np.ones_like(bits_1))
        arr = np.where(bits_1 == bits_2, np.nan * np.ones_like(bits_1), arr)
        
        return arr[~np.isnan(arr)].astype(np.int8)

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

                if unbiased and dep_seq_len > 1:
                    new_bitstring = np.array([], dtype=np.int8)
                    for i in range(gen_len // dep_seq_len):
                        sub_s1 = sample_1[i * dep_seq_len:(i+1) * dep_seq_len]
                        sub_s2 = sample_2[i * dep_seq_len:(i+1) * dep_seq_len]
                        postprocess_output = RNG.postprocess(sub_s1, sub_s2)
                        if np.size(postprocess_output):
                            new_bitstring = np.append(new_bitstring, np.array([postprocess_output[0]]))
                    
                else:
                    new_bitstring = RNG.postprocess(sample_1, sample_2)
                bitstring = np.append(bitstring, new_bitstring)
                pbar.update(len(new_bitstring))

        return np.copy(bitstring[:length]).astype(np.int8)

