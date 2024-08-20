"""The flyweight Concept by Farseen Ashraf"""


class IFlyweight:
    """Nothing to implement"""


class Flyweight(IFlyweight):
    """The concrete Flyweight"""

    def __init__(self, code: str) -> None:
        self.code = code


class FlyweightFactory:
    """Creating the Flyweight factory as a singleton"""

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
        """Return the number of flyweights in the cache"""
        return len(cls._flyweights)


class Context:
    """
    An example context that holds references to the flyweights in a
    particular order and convert the code to an ascii letter
    """

    def __init__(self, codes: str) -> None:
        self.codes = list(codes)

    def output(self):
        """The context specific output that uses flyweights"""
        ret = ""
        for code in self.codes:
            ret = ret + FlyweightFactory.get_flyweight(code=code).code
        return ret


# The Client
context = Context("abracadabra")

# Use flyweights in a context
print(context.output())

print(f"abracadabra has {len("abracadabra")} letters")
print(f"FlyweightFactory has {FlyweightFactory.get_count()} Flyweights")

