"""Abstract Factory Use Case Example Code By Farseen Ashraf"""

from furniture_factory import FurnitureFactory

product = FurnitureFactory.get_furniture("SmallChair")
print(f"{product.__class__}", product.get_dimensions())


product = FurnitureFactory.get_furniture("BigTable")
print(f"{product.__class__}", product.get_dimensions())
