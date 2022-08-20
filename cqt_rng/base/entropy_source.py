from abc import ABC, abstractmethod

class EntropySource(ABC):
    """
    TODO
    """
    @abstractmethod
    def __init__(self, **kwargs):
        """
        TODO
        """
        pass

    @abstractmethod
    def sample(self, length):
        """
        TODO
        """
        pass