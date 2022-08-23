"""This module contains the core class of the package which the RNG class. 
"""
import numpy as np
from tqdm import tqdm
from .entropy_source import EntropySource
from .post_processor import PostProcessor
from time import gmtime, strftime
from os import mkdir
from os.path import isdir


class RNG:
    """A Random Number Generator.

    Generates random numbers by taking two samples from the entropy_source and passing through the postprocessor.

    Parameters:
        entropy_source (EntropySource): The entropy source to sample from.
        postprocessor (PostProcessor): The post-processor.
        save_sample (bool, option): Whether to save the sample or not. Defaults to true.

    Examples:
        Generating a random bitstring of length 1024 using the BosonSampling as
        entropy source and the Von Neumann postprocessor::

            rng1 = RNG(BosonSampling(), VonNeumannPP())
            rng1.generate()
    """

    def __init__(
        self,
        entropy_source: EntropySource,
        postprocessor: PostProcessor,
        save_sample=True,
    ):
        self.entropy_source = entropy_source
        self.postprocessor = postprocessor
        self.save_sample = save_sample

    def generate(self, length=1024) -> np.ndarray:
        """Generates a random bitstring.

        Parameters:
            length (int): the length of the bitstring.

        Returns:
            nd.array: the random bitstring.
        """
        seq_len = self.entropy_source.seq_len
        bitstring = np.array([], dtype=np.int8)

        with tqdm(total=length) as pbar:
            while len(bitstring) < length:
                missing_length = length - len(bitstring)

                gen_len = 2 * seq_len * ((missing_length // seq_len) + 1)

                big_sample = self.entropy_source.sample(gen_len)
                if self.entropy_source.name != "Loader" and self.save_sample:
                    if not isdir("./data/"):
                        mkdir("./data/")
                    fname = (
                        "data/"
                        + self.entropy_source.name
                        + "_"
                        + strftime("%Y-%m-%d_%H-%M-%S", gmtime())
                    )
                    np.save(fname, big_sample)  # saving the sample

                total_length = len(big_sample)
                sample_1 = big_sample[: total_length // 2]
                sample_2 = big_sample[total_length // 2 :]

                new_bitstring = self.postprocessor.postprocess(sample_1, sample_2)
                bitstring = np.append(bitstring, new_bitstring)
                pbar.update(len(new_bitstring))

        return np.copy(bitstring[:length]).astype(np.int8)
