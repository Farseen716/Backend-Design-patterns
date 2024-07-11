"""Build concept Sample code by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class IBuilder(metaclass=ABCMeta):
    """Builder Interface class"""

    @staticmethod
    @abstractmethod
    def build_part_a():
        """Build part A"""

    @staticmethod
    @abstractmethod
    def build_part_b():
        """Build part A"""

    @staticmethod
    @abstractmethod
    def build_part_c():
        """Build part A"""

    @staticmethod
    @abstractmethod
    def get_result():
        """Return the final product"""


class Product:
    """The Product class"""
    def __init__(self):
        self.parts = []


class Builder(IBuilder):
    """Builder Concrete class which implements the builder interface"""

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append("a")
        return self

    def build_part_b(self):
        self.product.parts.append("b")
        return self

    def build_part_c(self):
        self.product.parts.append("c")
        return self

    def get_result(self):
        return self.product


class Director:
    """The Director class, which builds a complex representation"""

    @staticmethod
    def construct():
        """This builds and returns the final product"""
        return Builder().build_part_a().build_part_b().build_part_c().get_result()


PRODUCT = Director.construct()
print(PRODUCT.parts)
