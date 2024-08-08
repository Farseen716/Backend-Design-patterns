"""An interface to be implemented by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class ICubeA(metaclass=ABCMeta):
    """An interface for Cube A"""
    @staticmethod
    @abstractmethod
    def manufacture(width, height, depth):
        """Manufactures a cube using width, height and depth"""
