"""The Abstract Factory Interface By Farseen Ashraf"""
from abc import ABCMeta, abstractmethod


class IFurnitureFactory(metaclass=ABCMeta):
    """An interface for furniture factory"""

    @staticmethod
    @abstractmethod
    def get_furniture(furniture):
        """The static abstract method for furniture factory """
