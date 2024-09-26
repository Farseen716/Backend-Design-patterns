"""Thw Save/Restore game functionality by Farseen Ashraf"""


class Caretaker:
    """Guardian class which provides a narrow(simple) interface to the mementos"""

    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def save(self):
        """Stores a new Memento of the Characters current state"""
        print("Caretaker: Game Saved")
        memento = self._originator.memento
        self._mementos.append(memento)

    def restore(self, index):
        """
        Replace the Characters current attributes with the
        state stored in the saved Memento
        """
        print("Caretaker: Restoring Characters attributes from Mementos")
        memento = self._mementos[index]
        self._originator.memento = memento
