"""The Visitor Pattern Use Case Example by Farseen Ashraf"""
from abc import ABCMeta, abstractmethod


class IVisitor(metaclass=ABCMeta):
    """An interface that custom Visitors should implement"""
    @staticmethod
    @abstractmethod
    def visit(element):
        """Visitors visit Elements/Objects within the application"""


class IVisitable(metaclass=ABCMeta):
    """
    An interface the concrete objects should implement that allows
    the visitor to transverse a hierarchical structure of objects
    """
    @staticmethod
    @abstractmethod
    def accept(visitor):
        """
        The Visitor transverses and accesses each object
        through this method
        """


class AbstractCarPart:
    """The abstract car part"""

    @property
    def name(self):
        """A name for the part"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def sku(self):
        """The Stock Keeping Unit (sku)"""
        return self._sku

    @sku.setter
    def sku(self, value):
        self._sku = value

    @property
    def price(self):
        """The price per unit"""
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


class Body(AbstractCarPart, IVisitable):
    """A part of the car"""

    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.price = price

    def accept(self, visitor):
        visitor.visit(self)


class Engine(AbstractCarPart, IVisitable):
    """A part of the car"""

    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.price = price

    def accept(self, visitor):
        visitor.visit(self)


class Wheel(AbstractCarPart, IVisitable):
    """A part of the car"""

    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.price = price

    def accept(self, visitor):
        visitor.visit(self)


class Car(AbstractCarPart, IVisitable):
    """A Car with parts"""

    def __init__(self, name):
        self.name = name
        self._parts = [
            Body(name="Utility", sku="ABC-123-21", price=1001),
            Engine(name="V8 engine", sku="DEF-456-21", price=2555),
            Wheel(name="FrontLeft", sku="GHI-789FL-21", price=136),
            Wheel(name="FrontRight", sku="GHI-789SD-21", price=136),
            Wheel(name="BackLeft", sku="GHI-789MN-21", price=152),
            Wheel(name="BackRight", sku="GHI-789FG-21", price=152)
        ]

    def accept(self, visitor):
        for parts in self._parts:
            parts.accept(visitor)
        visitor.visit(self)


class PrintPartsVisitor(IVisitor):
    """Prints out the part name and sku"""

    @staticmethod
    def visit(element):
        if hasattr(element, "sku"):
            print(f"{element.name}\t:{element.sku}".expandtabs(6))


class TotalPriceVisitor(IVisitor):
    """Prints out the total cost of the parts in the car"""
    total_price = 0

    @classmethod
    def visit(cls, element):
        if hasattr(element, "price"):
            cls.total_price += element.price
        return cls.total_price


# The Client
car = Car("Delereon")

# prints out the part name and sku using the PrintPastsVisitor
car.accept(PrintPartsVisitor)

# Calculate the total price of the parts using the TotalPriceVisitor
total_price_visitor = TotalPriceVisitor()
car.accept(total_price_visitor)
print(f"Total Price = {total_price_visitor.total_price}")
