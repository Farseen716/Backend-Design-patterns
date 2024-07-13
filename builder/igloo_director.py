"""A Director class """
from house_builder import HouseBuilder


class IglooDirector:
    """One of the directors what build a complex representations"""

    @staticmethod
    def construct():
        """Construct and return the final product for Castle"""
        return HouseBuilder().\
            set_building_type('Igloo').\
            set_wall_material('Ice').\
            set_number_doors(1). \
            get_result()
