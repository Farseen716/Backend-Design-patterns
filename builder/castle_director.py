"""A Director class """
from house_builder import HouseBuilder


class CastleDirector:
    """One of the directors what build a complex representations"""

    @staticmethod
    def construct():
        """Construct and return the final product for Castle"""
        return HouseBuilder().\
            set_building_type('Castle').\
            set_wall_material('Sandstone').\
            set_number_doors(100).set_number_windows(200).\
            get_result()
