"""Singleton Design Pattern concept practice by Farseen Ashraf"""
import copy


class Singleton():
    value = []

    def __new__(cls):
        return cls

    # def __init__(self):
    #     print("In init")

    @classmethod
    def class_method(cls):
        """Use @classmethod to access class level variables"""
        print(cls.value)

    @staticmethod
    def static_method():
        """Use @staticmethod when no inner variables required"""


# The Client
# All uses of singleton points to the same memory address (id)
print(f"id(Singleton)\t = {id(Singleton)}")

OBJECT1 = Singleton()
print(f"id(OBJECT1)\t = {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t = {id(OBJECT2)}")

OBJECT3 = Singleton()
print(f"id(OBJECT3)\t = {id(OBJECT3)}")
