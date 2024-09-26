"""A proxy concept example by Farseen Ashraf"""

from abc import abstractmethod, ABCMeta


class ISubject(metaclass=ABCMeta):
    """An interface implemented by both the proxy and Real Subject"""
    @staticmethod
    @abstractmethod
    def request():
        """A method to implement"""


class RealSubject(ISubject):
    """The actual real object that the proxy is representing"""

    def __init__(self):
        self.enormous_data = [1, 2, 3]

    def request(self) -> list:
        return self.enormous_data


class Proxy(ISubject):
    """
    The proxy class. In this case the proxy will act as a cache for
    enormous data and only populate the enormous data when it is
    actually necessary
    """
    def __init__(self):
        self.enormous_list = []
        self.real_subject = RealSubject()

    def request(self):
        """
        Using the proxy as a cache, and loading data into it only
        if it is needed
        """
        if not self.enormous_list:
            print("Pulling data from Real Subject")
            self.enormous_list = self.real_subject.request()
            return self.enormous_list
        print("Pulling data from Proxy cache")
        return self.enormous_list


# The Client
subject = Proxy()
# use subject
print(id(subject))
# load the enormous amounts of data because now we want to show it
print(subject.request())
# Show the data again, but this time it retrieves it from the local cache
print(subject.request())

