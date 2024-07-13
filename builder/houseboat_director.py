"""A Director class """
from house_builder import HouseBuilder


class HouseBoatDirector:
    """One of the directors what build a complex representations"""

    @staticmethod
    def construct():
        """Construct and return the final product for Castle"""
        return HouseBuilder().\
            set_building_type('House Boat').\
            set_wall_material('Wood').\
            set_number_doors(6).set_number_windows(8).\
            get_result()
