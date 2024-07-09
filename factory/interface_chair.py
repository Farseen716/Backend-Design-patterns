""""The chair interface by Farseen Ashraf"""
from abc import ABCMeta, abstractmethod


class IChair(metaclass=ABCMeta):
    """The Chair Interface"""

    @staticmethod
    @abstractmethod
    def get_dimensions(self):
        """"The static interface method"""
