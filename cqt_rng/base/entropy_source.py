from abc import ABC, abstractmethod
import numpy as np


class EntropySource(ABC):
    """This is an abstract class from which you can generate random samples."""

    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def sample(self, length: int) -> np.ndarray:
        """Generates a sample.

        Parameters:
            length (int): the length of the sample.

        Returns:
            np.array: the sample.
        """
        pass
