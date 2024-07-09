"""The Factory Concept understanding by Farseen Ashraf"""
from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    """A Hypothetical Class Interface(Product)"""

    @staticmethod
    @abstractmethod
    def create_object():
        """An abstract interface method"""


class ConcreteProductA(IProduct):
    """A Concrete Class that implements IProduct interface"""

    def __init__(self):
        self.name = 'ConcreteProductA'

    def create_object(self):
        return self


class ConcreteProductB(IProduct):
    """A Concrete Class that implements IProduct interface"""

    def __init__(self):
        self.name = 'ConcreteProductB'

    def create_object(self):
        return self


class ConcreteProductC(IProduct):
    """A Concrete Class that implements IProduct interface"""

    def __init__(self):
        self.name = 'ConcreteProductC'

    def create_object(self):
        return self


class Creator:
    """The Factory Class"""

    @staticmethod
    def create_obj(some_property):
        """"A static method to get a concrete product"""

        if some_property == 'a':
            return ConcreteProductA()
        elif some_property == 'b':
            return ConcreteProductB()
        elif some_property == 'c':
            return ConcreteProductC()


# The Client
Product = Creator.create_obj('a')
print(Product.name)


