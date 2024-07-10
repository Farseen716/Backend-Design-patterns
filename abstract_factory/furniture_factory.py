"""Abstract Furniture Factory by Farseen Ashraf"""
from interface_furniture_factory import IFurnitureFactory
from chair_factory import ChairFactory
from table_factory import TableFactory


class FurnitureFactory(IFurnitureFactory):
    """The class of furniture factory which implements the interface of furniture factory"""

    @staticmethod
    def get_furniture(furniture):
        """"A static method of get furniture"""
        try:
            if furniture in ["SmallChair", "MediumChair", "BigChair"]:
                return ChairFactory.get_chair(furniture)
            if furniture in ["SmallTable", "MediumTable", "BigTable"]:
                return TableFactory.get_table(furniture)
            raise Exception("Factory not found")
        except Exception as _e:
            print(_e)
        return None
