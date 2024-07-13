"""The House Interface by Farseen Ashraf"""
from abc import ABCMeta, abstractmethod


class IHouseBuilder(metaclass=ABCMeta):
    """The Interface for House Builder"""

    @staticmethod
    @abstractmethod
    def set_building_type(building_type):
        """method to set the value for type of building"""

    @staticmethod
    @abstractmethod
    def set_wall_material(wall_material):
        """Method the set the value for material of the wall"""

    @staticmethod
    @abstractmethod
    def set_number_doors(number):
        """Method to set the number of doors in the building"""

    @staticmethod
    @abstractmethod
    def set_number_windows(number):
        """Method to set the number of windows in the building"""

    @staticmethod
    @abstractmethod
    def get_result():
        """Method to return the final product"""
