"""The State use case example"""
from abc import ABCMeta, abstractmethod


class Context:
    """This is the object whose behaviour will change"""

    def __init__(self):
        self.state_handles = [
            Started(),
            Running(),
            Finished()
        ]
        self._handle = iter(self.state_handles)

    def request(self):
        """Each time the request is called, a new class will handle it"""
        try:
            self._handle.__next__()()
        except StopIteration:
            # resetting so it loops
            self._handle = iter(self.state_handles)


class IState(metaclass=ABCMeta):
    """A State Interface"""

    @staticmethod
    @abstractmethod
    def __call__():
        """Set the default method"""


class Started(IState):
    """A ConcreteState subclass"""

    @staticmethod
    def method():
        """A task for this class"""
        print("Task Started")

    __call__ = method


class Running(IState):
    """A ConcreteState subclass"""

    @staticmethod
    def method():
        """A task for this class"""
        print("Task Running")

    __call__ = method


class Finished(IState):
    """A ConcreteState subclass"""

    @staticmethod
    def method():
        """A task for this class"""
        print("Task Finished")

    __call__ = method


# The Client
context = Context()
context.request()
context.request()
context.request()
context.request()
context.request()
context.request()
