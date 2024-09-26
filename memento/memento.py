"""A memento to store character attributes by Farseen Ashraf"""


class Memento:
    """A container of character attributes"""

    def __init__(self, score, inventory, level, location):
        self.score = score
        self.inventory = inventory
        self.level = level
        self.location = location
