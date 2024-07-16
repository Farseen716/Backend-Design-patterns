"""A game class which uses the Leaderboard Singleton"""

from interface_game import IGame
from leaderboard import Leaderboard


class Game1(IGame):
    """Concrete class which implements IGame"""
    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position=position, name=name)
