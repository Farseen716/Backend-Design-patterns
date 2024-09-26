"""
A Command object, which implements the ISwitch Interface and runs
the command on the designated receiver
"""

from interface_switch import ISwitch


class SwitchOnCommand(ISwitch):
    """Switch on command"""

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()
