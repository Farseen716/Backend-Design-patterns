"""Decorator Use Case Example Code by Farseen Ashraf"""

from add import Add
from sub import Sub
from value import Value

A = Value(1)
B = Value(2)
C = Value(5)

print(Add(A, B))
print(Add(A, 100))
print(Sub(C, A))
print(Sub(Add(C, B), A))
print(Sub(100, 101))
print(Add(Sub(Add(C, B), A), 100))
print(Sub(123, Add(C, C)))
print(Add(Sub(Add(C, 10), A), 100))
print(A)
print(B)
print(C)
