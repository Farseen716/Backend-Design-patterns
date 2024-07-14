"""A sample document to be used in the Prototype Use Case"""
import copy
from interface_prototype import IPrototype


class Document(IPrototype):
    """A concrete class which implements IPrototype interface"""

    def __init__(self, name, li):
        self.list = li
        self.name = name

    def clone(self, mode):
        """This clone method uses different cloning techniques"""

        if mode == 1:
            doc_list = self.list
            # results in 1 level shallow copy of the Document
        elif mode == 2:
            doc_list = self.list.copy()
            # results in 2 levels shallow copy of the Document
            # since it also create references for the 1st level
            # list elements as well
        elif mode == 3:
            doc_list = copy.deepcopy(self.list)
            # results in a deep copy creates by copying recursively at each index.
            # It is slower but results in a

        return type(self)(
            li=doc_list,
            name=self.name
        )

    def __str__(self):
        """Overriding the default __str__ method for our object"""
        return f"{id(self)}\tname={self.name}\tlist={self.list}"

