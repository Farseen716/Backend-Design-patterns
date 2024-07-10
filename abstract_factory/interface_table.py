"""The Table interface by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class ITable(metaclass=ABCMeta):
    """The Table Interface (Product)"""

    @staticmethod
    @abstractmethod
    def get_dimensions(self):
        """A static interface method"""
