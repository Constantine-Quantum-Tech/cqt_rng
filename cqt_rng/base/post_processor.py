from abc import ABC, abstractmethod
import numpy as np


class PostProcessor(ABC):
    """This is an abstract class from which you can produce post-processors.
    """

    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def postprocess(self, sample_1: np.ndarray, sample_2: np.ndarray) -> np.ndarray:
        """Takes two samples and returns the postprocessed bitstring.

        Returns:
            np.array: the postprocessed bitstring.
        """
        pass
