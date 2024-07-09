""""Chair Factory by Farseen Ashraf"""

from small_chair import SmallChair
from medium_chair import MediumChair
from big_chair import BigChair


class ChairFactory:
    """"A Chair Factory class"""

    @staticmethod
    def get_chair(size):
        """"A static method to get a chair"""
        if size == "small":
            return SmallChair()
        if size == "medium":
            return MediumChair()
        if size == "big":
            return BigChair()
        return None
