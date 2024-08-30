"""The Mediator Use Case Example by Farseen Ashraf"""

from component import Component
from mediator import Mediator

mediator = Mediator()
component_1 = Component(mediator=mediator, name="Component_1")
component_2 = Component(mediator=mediator, name="Component_2")
component_3 = Component(mediator=mediator, name="Component_3")
mediator.add(component_1)
mediator.add(component_2)
mediator.add(component_3)

component_1.notify("data A")
component_2.notify("data B")
component_3.notify("data C")
