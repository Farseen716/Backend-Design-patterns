"""A concrete class of chair of Farseen Ashraf"""
from interface_chair import IChair


class MediumChair(IChair):
    """The Medium Chair Concrete class implements IChair"""

    def __init__(self):
        self._width = 60
        self._depth = 60
        self._height = 60

    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }
