""""Sample code of FactoryB by Farseen Ashraf"""
from abc import abstractmethod, ABCMeta


class IProduct(metaclass=ABCMeta):
    """A hypothetical class interface (Product)"""

    @staticmethod
    @abstractmethod
    def create_object():
        """"An abstract interface method"""


class ConcreteProductA(IProduct):
    """"A concrete class that implements the IProduct Interface """

    def __init__(self):
        self.name = "ConcreteProductA"

    def create_object(self):
        return self


class ConcreteProductB(IProduct):
    """"A concrete class that implements the IProduct Interface """

    def __init__(self):
        self.name = "ConcreteProductB"

    def create_object(self):
        return self


class ConcreteProductC(IProduct):
    """"A concrete class that implements the IProduct Interface """

    def __init__(self):
        self.name = "ConcreteProductC"

    def create_object(self):
        return self


class FactoryB:
    """"The FactoryB class """

    @staticmethod
    def create_object(some_property):
        """A static method to get concrete product """
        try:
            if some_property == 'a':
                return ConcreteProductA()
            if some_property == 'b':
                return ConcreteProductB()
            if some_property == 'c':
                return ConcreteProductC()
            raise Exception("Class not found")
        except Exception as _e:
            print(_e)
        return None
