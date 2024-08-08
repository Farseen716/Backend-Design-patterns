"""An interface to be implemented by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class ICubeB(metaclass=ABCMeta):
    """An interface for an object"""
    @staticmethod
    @abstractmethod
    def create(top_left_front, bottom_right_back):
        """Manufactures a cube with coordinates offset [0,0,0]"""
