import random
import abc
from colors import Color

class Algorithm(metaclass=abc.ABCMeta):
    def __init__(self, size=100):
        self.data = []
        self.size = size
        self.color = Color

    def generate(self):
        self.data = []
        for i in range(self.size):
            random_value = random.randint(1, 150)
            self.data.append(random_value)
    
    @abc.abstractmethod
    def sort(self, drawData, timeTick):
        return
