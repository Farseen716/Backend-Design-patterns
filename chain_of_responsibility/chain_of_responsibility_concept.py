"""The Chain Of Responsibility pattern Concept by Farseen Ashraf"""
import random
from abc import ABCMeta, abstractmethod


class IHandler(metaclass=ABCMeta):
    """The Handler Interface that the successors should implement"""
    @staticmethod
    @abstractmethod
    def handle(payload):
        """A method to implement"""


class Successor1(IHandler):
    """A concrete handler"""

    @staticmethod
    def handle(payload):
        print(f"Successor1 Payload is {payload}")
        test = random.randint(1, 2)
        if test == 1:
            payload = payload + 1
            payload = Successor1().handle(payload=payload)
        elif test == 2:
            payload = payload - 1
            payload = Successor2().handle(payload=payload)
        return payload


class Successor2(IHandler):
    """A concrete handler"""

    @staticmethod
    def handle(payload):
        print(f"Successor2 Payload is {payload}")
        test = random.randint(1, 3)
        if test == 1:
            payload = payload * 2
            payload = Successor1().handle(payload=payload)
        elif test == 2:
            payload = payload / 2
            payload = Successor2().handle(payload=payload)
        return payload


class Chain:
    """A chain with the default first successor"""
    @staticmethod
    def start(payload):
        """Setting the first Successor that will modify the payload"""
        return Successor1().handle(payload=payload)


# The Client
chain = Chain()
payload = 1
out = chain.start(payload=payload)
print(f"Finished result = {out}")
