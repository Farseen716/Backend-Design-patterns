"""A memento pattern concept by Farseen Ashraf"""


class Memento:
    """A container of state"""

    def __init__(self, state):
        self.state = state


class Originator:
    """The object in the application whose state changes"""

    def __init__(self):
        self._state = ""

    @property
    def state(self):
        """A getter for the state of the object"""
        return self._state

    @state.setter
    def state(self, state):
        """A setter to set the value of state of the object"""
        print(f"Originator: Setting state to {state}")
        self._state = state

    @property
    def memento(self):
        """A getter for the state of the object but packaged as a Memento"""
        print(f"Originator: Providing memento of the state to caretaker.")
        return Memento(self._state)

    @memento.setter
    def memento(self, memento):
        self._state = memento.state
        print(f"Originator: State after restoring from Memento: "
              f" '{self._state}'")


class Caretaker:
    """Guardian. Provides a narrow interface to the mementos"""

    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def create(self):
        """Store a new Memento of the Originators current state"""
        print("Caretaker: Getting a copy of Originators current state")
        memento = self._originator.memento
        self._mementos.append(memento)

    def restore(self, index):
        """
        Replace the Originators current state with the state stored in
        the saved Memento
        """
        print("Caretaker: Restoring Originators state from Mementos")
        memento = self._mementos[index]
        self._originator.memento = memento


# The Client
originator = Originator()
caretaker = Caretaker(originator)

# Originators state can change periodically due to application events
originator.state = "State #1"
originator.state = "State #2"

# Lets backup the originators
caretaker.create()

# more changes,  and then another backup
originator.state = "State #3"
caretaker.create()

# more changes
originator.state = "State #4"
print(originator.state)
print()

# Restore from the first backup
caretaker.restore(0)
print(originator.state)
print()

# Restore from second backup
caretaker.restore(1)
print(originator.state)
