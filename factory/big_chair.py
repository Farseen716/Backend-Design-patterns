""" Class for Big Chair by Farseen Ashraf"""
from interface_chair import IChair


class BigChair(IChair):
    """A Big Chair class which implements IChair interface """

    def __init__(self):
        self._height = 80  # the use of underscore makes it a protected variable
        self._width = 80  # the use of underscore makes it a protected variable
        self._depth = 80  # the use of underscore makes it a protected variable

    def get_dimensions(self):
        return {
            "height": self._height,
            "width": self._width,
            "depth": self._depth
        }
