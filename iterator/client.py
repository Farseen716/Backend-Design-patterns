"""The Iterator Pattern Concept"""


class NumberWheel():
    """The concrete iterator (iterable)"""

    def __init__(self):
        self.index = 0

    def next(self):
        """Returns a new number next in the wheel"""
        self.index = self.index + 1
        return self.index * 2 % 11


# The Client
number_wheel_a = NumberWheel()
number_wheel_b = NumberWheel()

for i in range(5):
    print(number_wheel_a.next(), end=", ")

for i in range(5):
    print(number_wheel_b.next(), end=", ")
