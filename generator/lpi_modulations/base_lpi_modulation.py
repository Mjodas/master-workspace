from abc import ABC, abstractmethod

class BaseLPIModulation(ABC):

    # abstract method
    def generate_sample(self):
        pass

    # abstract method
    def generate_random_sample(self):
        pass

    # abstract method
    def create_spectogram(self):
        pass