"""The Table Factory Class by Farseen Ashraf"""

from small_table import SmallTable
from medium_table import MediumTable
from big_table import BigTable


class TableFactory:
    """The factory class"""

    @staticmethod
    def get_table(table):
        """A static method to get a table"""
        try:
            if table == "SmallTable":
                return SmallTable()
            if table == "MediumTable":
                return MediumTable()
            if table == "BigTable":
                return BigTable()
            raise Exception("Class not found")
        except Exception as _e:
            print(_e)
        return None
