"""The Chair interface by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class IChair(metaclass=ABCMeta):
    """The Chair Interface (Product)"""

    @staticmethod
    @abstractmethod
    def get_dimensions(self):
        """A static interface method"""
