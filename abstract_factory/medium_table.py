"""A concrete class of table of Farseen Ashraf"""
from interface_table import ITable


class MediumTable(ITable):
    """The Medium Table Concrete class implements ITable"""

    def __init__(self):
        self._width = 110
        self._depth = 60
        self._height = 70

    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }
