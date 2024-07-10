"""The Chair Factory Class by Farseen Ashraf"""

from small_chair import SmallChair
from medium_chair import MediumChair
from big_chair import BigChair


class ChairFactory:
    """The factory class"""

    @staticmethod
    def get_chair(chair):
        """A static method to get a chair"""
        try:
            if chair == "SmallChair":
                return SmallChair()
            if chair == "MediumChair":
                return MediumChair()
            if chair == "BigChair":
                return BigChair()
            raise Exception("Class not found")
        except Exception as _e:
            print(_e)
        return None
