"""The Interpreter Pattern Concept by Farseen Ashraf"""


class AbstractExpression:
    """All Terminal and Non-Terminal expressions will implement
    an 'interpret' method"""

    @staticmethod
    def interpret():
        """
        The 'interpret' method gets called recursively for each
        AbstractExpression
        """


class Number(AbstractExpression):
    """Terminal Expression"""

    def __init__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

    def __repr__(self):
        return str(self.value)


class Add(AbstractExpression):
    """Non-Terminal Expression"""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

    def __repr__(self):
        return f"({self.left} Add {self.right})"


class Subtract(AbstractExpression):
    """Non-Terminal Expression"""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

    def __repr__(self):
        return f"({self.left} Subtract {self.right})"


# The Client
# The sentence compiles with a simple grammar of
# Number -> Operator -> Number -> etc,
sentence = "5 + 4 - 3 + 7 - 2"
print(sentence)

# Split the sentence into individual expressions that will be added to
# an Abstract System Tree (AST) as Terminal and Non-Terminal expressions
tokens = sentence.split(" ")
print(tokens)

# Manually creating an Abstract Syntax Tree from the tokens
ast: list[AbstractExpression] = []
ast.append(Add(Number(tokens[0]), Number(tokens[2])))  # 5 + 4
ast.append(Subtract(ast[0], Number(tokens[4])))  # ^ - 3
ast.append(Add(ast[1], Number(tokens[6])))
ast.append(Subtract(ast[2], Number(tokens[8])))

# Use the final AST row as the root node
ast_root = ast.pop()

# Interpreter recursively through the full AST starting from the root
print(ast_root.interpret())

# print out the representation of the ast_root
print(ast_root)
