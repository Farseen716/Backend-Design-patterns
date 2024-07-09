""""Factory use case example by Farseen Ashraf"""
from chair_factory import ChairFactory

# The client
product = ChairFactory.get_chair("medium")
print(product.get_dimensions())
