"""Singleton use case example by Farseen Ashraf"""

from game_1 import Game1
from game_2 import Game2
from game_3 import Game3

# The Client
# All games share and manages the same Leaderboard because it is a singleton

GAME1 = Game1()
GAME1.add_winner(position=2, name="Fahad")

GAME2 = Game2()
GAME2.add_winner(position=1, name="Farseen")

GAME3 = Game3()
GAME3.add_winner(position=3, name="Furqan")

GAME1.leaderboard.print()
GAME2.leaderboard.print()
GAME3.leaderboard.print()

