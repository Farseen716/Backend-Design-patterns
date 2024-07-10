"""A concrete class of chair of Farseen Ashraf"""
from interface_chair import IChair


class BigChair(IChair):
    """The Big Chair Concrete class implements IChair"""

    def __init__(self):
        self._width = 80
        self._depth = 80
        self._height = 80

    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }
