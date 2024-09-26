"""The strategy pattern example use case by Farseen Ashraf"""
from abc import ABCMeta, abstractmethod


class GameCharacter:
    """This is the context whose strategy will change"""

    position = [0, 0]

    @classmethod
    def move(cls, movement_style):
        """The movement algorithm has been decided by the client"""
        movement_style(cls.position)


class IMove(metaclass=ABCMeta):
    """A concrete strategy interface"""

    @staticmethod
    @abstractmethod
    def __call__():
        """Implementers must select the default method"""


class Walking(IMove):
    """A concrete strategy subclass"""

    @staticmethod
    def walk(position):
        """A walk algorithm"""
        position[0] += 1
        print(f"I am Walking. New position = {position}")

    __call__ = walk


class Running(IMove):
    """A concrete strategy subclass"""

    @staticmethod
    def run(position):
        """A walk algorithm"""
        position[0] += 2
        print(f"I am Running. New position = {position}")

    __call__ = run


class Crawling(IMove):
    """A concrete strategy subclass"""

    @staticmethod
    def crawl(position):
        """A walk algorithm"""
        position[0] += 0.5
        print(f"I am Crawling. New position = {position}")

    __call__ = crawl


#  The Client
game_character = GameCharacter()
game_character.move(Walking())

# Character sees the enemy
game_character.move(Running())

# Character sees a small cave to hide in
game_character.move(Crawling())

