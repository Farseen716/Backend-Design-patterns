"""The interpreter pattern use case example by Farseen Ashraf"""

from sentence_parser import Parser


# The sentence compiles with a simple grammar
# of Number -> Operator -> Number etc,
sentence = "5 + IV - 3 + VII - 2"
# sentence = "V + IV - III + 7 -II"
# sentence = "CIX + V - 3 + VII - 2"
# sentence = "MMMCMXCIX + CXIX + MCXXII - MMMCDXII - XVIII - CCXXXV"
print(sentence)

ast_root = Parser.parse(sentence)

# Interpret recursively through the full ast starting from the root
print(ast_root.interpret())

# print out a representation of the ast_root
print(ast_root)
