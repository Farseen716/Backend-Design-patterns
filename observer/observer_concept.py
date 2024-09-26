"""observer Design Pattern Concept by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class IObservable(metaclass=ABCMeta):
    """The Subject Interface"""

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        """The subscribe method"""

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        """The unsubscribe method"""

    @staticmethod
    @abstractmethod
    def notify(observer):
        """The notify method"""


class Subject(IObservable):
    """The Subject (a.k.a Observable)"""

    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *args):
        for observer in self._observers:
            observer.notify(*args)


class IObserver(metaclass=ABCMeta):
    """A class for the observer to implement"""

    @staticmethod
    @abstractmethod
    def notify(observable, *args):
        """Receive notifications"""


class Observer(IObserver):
    """The concrete class that implements IObserver"""

    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, *args):
        print(f"observer id: {id(self)} received {args} ")


# The Client
subject = Subject()
observer_a = Observer(subject)
observer_b = Observer(subject)

subject.notify("First Notification", [1, 2, 3])
subject.unsubscribe(observer_b)
subject.notify("Second Notification", {"A": 1, "B": 2, "C": 3})
