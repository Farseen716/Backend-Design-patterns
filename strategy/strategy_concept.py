"""The Strategy pattern concept"""

from abc import ABCMeta, abstractmethod


class Context:
    """This is the object whose behaviour will change"""

    @staticmethod
    def request(strategy):
        """This request is handled by the class passed in"""
        return strategy


class IStrategy(metaclass=ABCMeta):
    """A strategy interface"""
    @staticmethod
    @abstractmethod
    def __str__():
        """Implement the __str__ dunder"""


class ConcreteStrategyA(IStrategy):
    """A concrete strategy subclass"""

    def __str__(self):
        return "I am ConcreteStrategyA"


class ConcreteStrategyB(IStrategy):
    """A concrete strategy subclass"""

    def __str__(self):
        return "I am ConcreteStrategyB"


class ConcreteStrategyC(IStrategy):
    """A concrete strategy subclass"""

    def __str__(self):
        return "I am ConcreteStrategyC"


# The Client
context = Context()

print(context.request(ConcreteStrategyA()))
print(context.request(ConcreteStrategyB()))
print(context.request(ConcreteStrategyC()))
