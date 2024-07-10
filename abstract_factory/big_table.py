"""A concrete class of table of Farseen Ashraf"""
from interface_table import ITable


class BigTable(ITable):
    """The Big Table Concrete class implements ITable"""

    def __init__(self):
        self._width = 120
        self._depth = 60
        self._height = 80

    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }
