"""A Data View Interface by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class IDataView(metaclass=ABCMeta):
    """A Subject Interface"""

    @staticmethod
    @abstractmethod
    def notify(observer):
        """Receive notifications"""

    @staticmethod
    @abstractmethod
    def draw(observer_id):
        """Draw the view"""

    @staticmethod
    @abstractmethod
    def delete(data):
        """A delete method to remove observer
        specific resources"""
