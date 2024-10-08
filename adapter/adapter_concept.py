"""Adaptor Concept Code by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class IA(metaclass=ABCMeta):
    """An interface for an object"""

    @staticmethod
    @abstractmethod
    def method_a():
        """An abstract method A"""


class ClassA(IA):
    """The class which implements the interface IA"""
    def method_a(self):
        print("Method A")


class IB(metaclass=ABCMeta):
    """An interface for an object"""

    @staticmethod
    @abstractmethod
    def method_b():
        """An abstract method B"""


class ClassB(IB):
    """The class which implements the interface IB"""
    def method_b(self):
        print("Method B")


class ClassBAdapter(IA):
    """class B does not have a method_a, so we need to create an adapter"""
    def __init__(self):
        self.class_b = ClassB()

    def method_a(self):
        self.class_b.method_b()

# The Client
# Before the adapter, I need to test the objects class to know which
# method to call


ITEMS = [ClassA(), ClassB()]

for item in ITEMS:
    if isinstance(item, ClassB):
        item.method_b()
    else:
        item.method_a()

# After create an Adapter for class B, I can use the same method
# signature as ClassA (preferred)
ITEMS = [ClassA(), ClassBAdapter()]

for item in ITEMS:
    item.method_a()
