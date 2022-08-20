from abc import ABC, abstractmethod

class PostProcessor(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        pass
    
    @abstractmethod
    def postprocess(self, sample_1, sample_2):
        pass