"""A game interface by Farseen Ashraf"""
from abc import ABCMeta, abstractmethod


class IGame(metaclass=ABCMeta):
    """Interface for the Game"""

    @staticmethod
    @abstractmethod
    def add_winner(position, name):
        """Method to add winner of the game"""
