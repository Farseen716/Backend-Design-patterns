"""The game api facade by Farseen Ashraf"""

from decimal import Decimal
from game_engine import GameEngine
from reports import Reports
from users import Users
from wallets import Wallets


class GameApi:
    """The GameApi Facade for the client"""
    @staticmethod
    def get_balance(user_id: str) -> Decimal:
        """Get the balance for the player"""
        return Wallets.get_balance(user_id=user_id)

    @staticmethod
    def game_state() -> dict:
        """Get the current game state"""
        return GameEngine.get_game_state()

    @staticmethod
    def get_history():
        """Get the history of the game"""
        return Reports.get_history()

    @staticmethod
    def change_pwd(user_id: str, password: str) -> bool:
        """Change the password of the user"""
        return Users.change_pwd(user_id=user_id, pwd=password)

    @staticmethod
    def submit_entry(user_id: str, entry: Decimal) -> bool:
        """Submit a bet by the user"""
        return GameEngine().submit_entry(user_id=user_id, entry=entry)

    @staticmethod
    def register_user(value: dict[str, str]) -> str:
        """Register a new user and return the id"""
        return Users.register_user(new_user=value)
