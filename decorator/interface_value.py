"""The interface that the Value class must implement by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class IValue(metaclass=ABCMeta):
    """Methods the component must implement"""
    @staticmethod
    @abstractmethod
    def __str__():
        """Overrides the object to return the value attribute by default"""
