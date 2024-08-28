"""The Command Pattern Concept by Farseen Ashraf"""

from abc import ABCMeta, abstractmethod


class ICommand(metaclass=ABCMeta):
    """The Command Interface that all commands will implement"""

    @staticmethod
    @abstractmethod
    def execute():
        """The required execute method that all command objects will use"""


class Invoker:
    """The Invoker class"""

    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        """Register commands in the Invoker"""
        self._commands[command_name] = command

    def execute(self, command_name):
        """Execute any registered commands"""

        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognized")


class Receiver:
    """The Receiver"""

    @staticmethod
    def run_command_1():
        """A set of instructions to run"""
        print("Executing Command 1")

    @staticmethod
    def run_command_2():
        """A set of instructions to run"""
        print("Executing Command 2")


class Command1(ICommand):
    """
    A Command object, that implements the ICommand Interface and
    runs the command on the designated receiver
    """

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_1()


class Command2(ICommand):
    """
    A Command object, that implements the ICommand Interface and
    runs the command on the designated receiver
    """

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_2()


# Create the receiver

receiver_ = Receiver()

# Create Commands
command_1 = Command1(receiver=receiver_)
command_2 = Command2(receiver=receiver_)

# Register the command with the Invoker
invoker = Invoker()
invoker.register(command_name="1", command=command_1)
invoker.register(command_name="2", command=command_2)

# Execute the commands that are registered on the Invoker
invoker.execute("1")
invoker.execute("2")
invoker.execute("1")
invoker.execute("2")
