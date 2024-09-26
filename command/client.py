"""The Command Pattern use case example by Farseen Ashraf"""

from light import Light
from switch import Switch
from switch_off_command import SwitchOffCommand
from switch_on_command import SwitchOnCommand


# Create a receiver
light = Light()

# create commands
switch_on = SwitchOnCommand(light=light)
switch_off = SwitchOffCommand(light=light)

# Register the commands with the invoker
switch = Switch()
switch.register(command_name="ON", command=switch_on)
switch.register(command_name="OFF", command=switch_off)

# Execute the commands that are registered on the Invoker
switch.execute("ON")
switch.execute("OFF")
switch.execute("ON")
switch.execute("OFF")

# show history
switch.show_history()

# replay last 2 executed commands
switch.replay_last(number_of_commands=2)
