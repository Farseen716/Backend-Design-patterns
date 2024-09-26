"""Creating the flyweight factory as a singleton"""
from flyweight import Flyweight


class FlyweightFactory:
    """Creating the FlyweightFactory as a singleton"""

    _flyweights: dict[str, Flyweight] = {}

    def __new__(cls):
        return cls

    @classmethod
    def get_flyweight(cls, code: str) -> Flyweight:
        """A static method to get a flyweight based on a code"""
        if code not in cls._flyweights:
            cls._flyweights[code] = Flyweight(code)
        return cls._flyweights[code]

    @classmethod
    def get_count(cls) -> int:
        "return the number of flyweights in the cache"
        return len(cls._flyweights)
