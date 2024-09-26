"""Subtract Expression. This is a Non-Terminal Expression by Farseen Ashraf"""

from abstract_expression import AbstractExpression


class Subtract(AbstractExpression):
    """Non-Terminal Expression"""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

    def __repr__(self):
        return f"({self.left} Add {self.right})"
