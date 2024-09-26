"""Bridge Design Pattern Concept Sample Code by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class IAbstraction(metaclass=ABCMeta):
    """The Abstraction Interface"""
    @staticmethod
    @abstractmethod
    def method():
        """The method handle"""


class RefinedAbstractionA(IAbstraction):
    """A refined Abstraction"""
    def __init__(self, implementer):
        self.implementer = implementer()

    def method(self, *args):
        self.implementer.method(*args)


class RefinedAbstractionB(IAbstraction):
    """A refined Abstraction"""

    def __init__(self, implementer):
        self.implementer = implementer()

    def method(self, *args):
        self.implementer.method(*args)


class IImplementer(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method(*args: tuple) -> None:
        """The method implementation"""


class ConcreteImplementerA(IImplementer):
    """A concrete class"""

    @staticmethod
    def method(*args: tuple) -> None:
        print(args)


class ConcreteImplementerB(IImplementer):
    """A concrete class"""

    @staticmethod
    def method(*args: tuple) -> None:
        for arg in args:
            print(arg)


# The Client
refined_abstraction_A = RefinedAbstractionA(ConcreteImplementerA)
refined_abstraction_A.method('a',  'b', 'c')

refined_abstraction_B = RefinedAbstractionB(ConcreteImplementerB)
refined_abstraction_B.method('a',  'b', 'c')

