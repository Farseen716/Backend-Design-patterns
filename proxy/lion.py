"""A Lion class by Farseen Ashraf"""
import random

from interface_proteus import IProteus
import serpent
import leopard


class Lion(IProteus):
    """Proteus in the form of a Lion"""

    name = "Lion"

    def tell_me_the_future(self):
        """Proteus will change to something randomly"""
        self.__class__ = leopard.Leopard if random.randint(0, 1) else serpent.Serpent

    @classmethod
    def tell_me_your_form(cls):
        print("I am the form of a " + cls.name)

