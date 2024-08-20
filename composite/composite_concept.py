"""Composite design pattern concept by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):
    """
    A composite interface describing the common methods and fields
    for leaves and composites
    """
    reference_to_parent = None

    @staticmethod
    @abstractmethod
    def method():
        """A method each leaf and composite container should implement"""

    @staticmethod
    @abstractmethod
    def detach():
        """Called before a leaf is attached to a composite"""


class Leaf(IComponent):
    """A Leaf can be added to a composite, but not a leaf"""

    def method(self):
        parent_id = (id(self.reference_to_parent) if
                     self.reference_to_parent is not None else None)
        print(
            f"<Leaf>\t\tid:{id(self)}\tParent:\t{parent_id}"
        )

    def detach(self):
        """Detaching this leaf from its parent composite"""
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)


class Composite(IComponent):
    """A composite can contain leaves and composites"""

    def __init__(self):
        self.components = []

    def method(self):
        parent_id = (id(self.reference_to_parent) if
                     self.reference_to_parent is not None else None)
        print(
            f"<Composite>\tid:{id(self)}\tParent:\t{parent_id}"
            f"Components:{len(self.components)}"
        )

        for component in self.components:
            component.method()

    def attach(self, component):
        """Detach leaf/composite from any current parent reference and
         then set the parent reference to this composite(self)"""
        component.detach()
        component.reference_to_parent = self
        self.components.append(component)

    def delete(self, component):
        """Removes leaf/composite from this composite self.components"""
        self.components.remove(component)

    def detach(self):
        """Detatching this component from its parent composite"""
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)
            self.reference_to_parent = None


# The Client
leaf_a = Leaf()
leaf_b = Leaf()
composite_1 = Composite()
composite_2 = Composite()

print(f"Leaf_a\t\tid:{id(leaf_a)}")
print(f"Leaf_b\t\tid:{id(leaf_b)}")
print(f"composite_1\t\tid:{id(composite_1)}")
print(f"composite_2\t\tid:{id(composite_2)}")

# Attach leaf_a to composite_1
composite_1.attach(leaf_a)

# Instead attach leaf_a to composite_2
composite_2.attach(leaf_a)

# Attach composite_1 to composite_2
composite_2.attach(composite_1)

print()
leaf_b.method()        # not in any composite
composite_2.method()    # composite_2 contains both composite_1 and leaf_a
