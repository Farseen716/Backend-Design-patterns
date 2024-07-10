"""A concrete class of chair of Farseen Ashraf"""
from interface_chair import IChair


class SmallChair(IChair):
    """The Small Chair Concrete class implements IChair"""

    def __init__(self):
        self._width = 40
        self._depth = 40
        self._height = 40

    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }
