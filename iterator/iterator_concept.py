"""The iterator Pattern Concept by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class IIterator(metaclass=ABCMeta):
    """
    An iterator interface
    """
    @staticmethod
    @abstractmethod
    def has_next():
        """Returns Boolean whether at end of collection or not"""

    @staticmethod
    @abstractmethod
    def next():
        """Returns the object in collection"""


class Iterable(IIterator):
    """The concrete iterator (iterable)"""

    def __init__(self, aggregates):
        self.index = 0
        self.aggregates = aggregates

    def next(self):
        if self.index < len(self.aggregates):
            aggregate = self.aggregates[self.index]
            self.index += 1
            return aggregate
        raise Exception("AtEndOfIteratorException", "At End of Iterator")

    def has_next(self):
        return self.index < len(self.aggregates)


class IAggregate(metaclass=ABCMeta):
    """An interface that the aggregates should implement"""

    @staticmethod
    @abstractmethod
    def method():
        """A method to implement"""


class Aggregate(IAggregate):
    """A concrete object"""
    @staticmethod
    def method():
        print("This method has been invoked")


# The Client
aggregates = [Aggregate(), Aggregate(), Aggregate(), Aggregate]

# aggregates is a python list that is already iterable by default
# but we can create our own iterator on top anyway

iterable = Iterable(aggregates=aggregates)

while iterable.has_next():
    iterable.next().method()

# print()
# for a in aggregates:
#     a.method()
