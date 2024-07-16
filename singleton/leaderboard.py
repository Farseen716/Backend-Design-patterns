"""A Leaderboard class which uses Singleton design pattern by Farseen Ashraf """


class Leaderboard():
    """A Leaderboard class"""
    _table = {}

    def __new__(cls):
        return cls

    @classmethod
    def print(cls):
        """A class level method to print the values"""
        print("---------- Leaderboard ----------")
        for key, value in sorted(cls._table.items()):
            print(f"|\t{key}\t|\t{value}")
        print()

    @classmethod
    def add_winner(cls, position, name):
        """A class method to add a winner name against his position"""
        cls._table[position] = name
