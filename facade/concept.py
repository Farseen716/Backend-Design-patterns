"""The Facade pattern concept by Farseen Ashraf"""


class SubSystemClassA:
    """A hypothetically complex class"""
    @staticmethod
    def method():
        """A hypothetically complex method"""
        return "A"


class SubSystemClassB:
    """A hypothetically complex class"""
    @staticmethod
    def method(value):
        """A hypothetically complex method"""
        return value


class SubSystemClassC:
    """A hypothetically complex class"""
    @staticmethod
    def method(value):
        """A hypothetically complex method"""
        return value


class Facade:
    """A simplified facade, offering the services of all the subsystems"""
    @staticmethod
    def sub_system_class_a():
        """Use the sub system methods"""
        return SubSystemClassA.method()

    @staticmethod
    def sub_system_class_b(value):
        """Use the sub system methods"""
        return SubSystemClassB.method(value=value)

    @staticmethod
    def sub_system_class_c(value):
        """Use the sub system methods"""
        return SubSystemClassC.method(value=value)


# The Client
# Call the complicated subsystems directly
print(SubSystemClassA.method())
print(SubSystemClassB.method("B"))
print(SubSystemClassC.method({"C": [1, 2, 3]}))

# or use the simplified facade
print(Facade().sub_system_class_a())
print(Facade().sub_system_class_b("B"))
print(Facade().sub_system_class_c({"C": [1, 2, 3]}))
