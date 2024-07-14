"""Prototype concept by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class IPrototype(metaclass=ABCMeta):
    """Interface class containing the clone"""

    @staticmethod
    @abstractmethod
    def clone():
        """The clone method which makes deep or shallow copy of the object.
        It is up to you how you want to implement the details in the concrete
        class"""


class MyClass(IPrototype):
    """Concrete class that implements the IPrototype interface"""

    def __init__(self, fields):
        self.fields = fields

    def clone(self):
        """This clone method uses a shallow copy technique"""
        return type(self)(  # type(self) basically is used to give a new instance of class MyClass
            self.fields  # in the instance we pass the fields value in the constructor and a shallow copy
            # is returned
            # self.fields.copy()  # this is also a shallow copy, but has also shallow copied the
            # first level of the field. So it is essentially a shallow copy but 2 levels deep.
        )

    def __str__(self):
        return f"{id(self)}\tfield={self.fields}\ttype={type(self.fields)}"


# The Client
OBJECT1 = MyClass([1, 2, 3, 4])
print(f"OBJECT1 {OBJECT1}")

OBJECT2 = OBJECT1.clone()

# Change the value of one of the list elements in OBJECT2,
# to see if it also modifies the list element in OBJECT1.
# If it changed OBJECT1s copy also, then the clone was done
# using a 1 level shallow copy process.
# Modify the clone method above to try a 2 level shallow copy instead
# and compare the output

OBJECT2.fields[1] = 200
print(f"OBJECT1 {OBJECT1}")
print(f"OBJECT2 {OBJECT2}")

