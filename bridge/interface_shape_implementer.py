"""A Shape implementer interface by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class IShapeImplementer(metaclass=ABCMeta):
    """Shape implementer"""

    @staticmethod
    @abstractmethod
    def draw_implementation():
        """The method that the refined abstractions will implement"""
