"""The house builder class by Farseen Ashraf"""

from interface_house_builder import IHouseBuilder
from house import House


class HouseBuilder(IHouseBuilder):
    """The Concrete class which implements the IHouseBuilder Interface"""

    def __init__(self):
        self.house = House()

    def set_number_doors(self, number):
        self.house.doors = number
        return self

    def set_number_windows(self, number):
        self.house.windows = number
        return self

    def set_building_type(self, building_type):
        self.house.building_type = building_type
        return self

    def set_wall_material(self, wall_material):
        self.house.wall_material = wall_material
        return self

    def get_result(self):
        return self.house
