"""Decorator Concept Sample Code By Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):
    """Interface whose methods must be implemented by Component class"""
    @staticmethod
    @abstractmethod
    def method():
        """A method to be implemented"""


class Component(IComponent):
    """A Component that can be implemented or not"""
    def method(self):
        """Method of the Component class"""
        return "Component Method"


class Decorator(IComponent):
    """Decorator also implements the IComponent Interface"""
    def __init__(self, obj):
        """Set a reference to the decorated object"""
        self.object = obj

    def method(self):
        """Method of the Decorator class"""
        return f"Decorator Method ({self.object.method()})"


# The Client
component = Component()
print(component.method())
print(Decorator(component).method())
print(Decorator(Decorator(component)).method())
print(component.method())

