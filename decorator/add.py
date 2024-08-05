"""The Addition Decorator by Farseen Ashraf"""

from interface_value import IValue


class Add(IValue):
    """A decorator that adds a number to another number"""

    def __init__(self, val1, val2):
        """val1 and val2 can be int or the custom value
        objects that contain the 'value' attribute"""
        val1 = getattr(val1, 'value', val1)
        val2 = getattr(val2, 'value', val2)
        self.value = val1 + val2

    def __str__(self):
        return str(self.value)
