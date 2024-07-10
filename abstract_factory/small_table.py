"""A concrete class of table of Farseen Ashraf"""
from interface_table import ITable


class SmallTable(ITable):
    """The Small Table Concrete class implements ITable"""

    def __init__(self):
        self._width = 100
        self._depth = 60
        self._height = 60

    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }
