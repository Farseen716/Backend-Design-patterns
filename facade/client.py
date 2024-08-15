"""The Facade example use case by Farseen Ashraf"""
import time
from decimal import Decimal
from game_api import GameApi

user = {"user_name": "Sean"}
user_id = GameApi.register_user(value=user)

time.sleep(1)

GameApi.submit_entry(user_id=user_id, entry=Decimal('5'))

time.sleep(1)

print()
print("----- Game Snapshot -----")
print(GameApi.game_state())

time.sleep(1)


history = GameApi.get_history()

print()
print("----- Game History -----")
for row in history:
    print(f"{row} : {history[row][0]} : {history[row][1]}")

print()
print("----- Game Snapshot -----")
print(GameApi.game_state())
