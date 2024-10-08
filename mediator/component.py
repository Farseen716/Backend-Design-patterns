"""Component class by Farseen Ashraf"""

from interface_component import IComponent


class Component(IComponent):
    """Each component stays synchronized through a mediator"""

    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name

    def notify(self, message):
        """Component is notifying mediator of a message"""
        print(self._name + ": >>> Out : " + message )
        self._mediator.notify(message, self)

    def receive(self, message):
        print(self._name + ": <<< In <<< : " + message)
