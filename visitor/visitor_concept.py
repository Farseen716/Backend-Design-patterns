"""The visitor concept pattern by Farseen Ashraf"""
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


class Element(IVisitable):
    """An object can be part of any hierarchy"""

    def __init__(self, name, value, parent=None):
        self.name = name
        self.value = value
        self.elements = set()
        if parent:
            parent.elements.add(self)

    def accept(self, visitor):
        """this method is required by the Visitor that will transverse"""
        for element in self.elements:
            element.accept(visitor)
        visitor.visit(self)


#  The Client
# Creating an example object hierarchy
element_a = Element(name="A", value=101)
element_b = Element(name="B", value=305, parent=element_a)
element_c = Element(name="C", value=185, parent=element_a)
element_d = Element(name="D", value=-30, parent=element_b)

# now rather than changing the Element class to support custom
# operations, we can utilise the accept method that was
# implemented in the Element class because of the addition
# of the IVisitable interface


class PrintElementNamesVisitor(IVisitor):
    """Create a visitor that prints the Elements names"""
    @staticmethod
    def visit(element):
        print(element.name)


# Using the PrintElementNamesVisitor to transverse the object hierarchy
element_a.accept(PrintElementNamesVisitor)


class CalculateElementsTotalVisitors(IVisitor):
    """Create a visitor that totals the Elements values"""
    total_value = 0

    @classmethod
    def visit(cls, element):
        cls.total_value += element.value
        return cls.total_value


# Using the CalculateElementsTotalVisitors to
# transverse the object hierarchy
total = CalculateElementsTotalVisitors()
element_a.accept(CalculateElementsTotalVisitors)
print(total.total_value)
