"""Prototype Concept sample code by Farseen Ashraf"""
from abc import ABCMeta, abstractmethod


class IPrototype(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def clone(mode):
        """The clone method which can make either deep or shallow copy.
        It is up to you how you want to implement the details in
        the concrete class"""
