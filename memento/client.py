"""Memento example Use Case"""

from game_character import GameCharacter
from caretaker import Caretaker

game_character = GameCharacter()
caretaker = Caretaker(game_character)

# start the game
game_character.register_kill()
game_character.move_forward(amount=1)
game_character.add_inventory(item="sword")
game_character.register_kill()
game_character.add_inventory(item="rifle")
game_character.move_forward(amount=1)
print(game_character)

# save the progress
caretaker.save()

game_character.register_kill()
game_character.move_forward(amount=1)
game_character.progress_to_next_level()
game_character.register_kill()
game_character.add_inventory(item="motorbike")
game_character.move_forward(amount=10)
game_character.register_kill()
print(game_character)

# save progress
caretaker.save()

game_character.move_forward(amount=1)
game_character.progress_to_next_level()
game_character.register_kill()
print(game_character)

# decide you made a mistake, go back to first move
caretaker.restore(index=0)
print(game_character)

# continue
game_character.register_kill()
