"""A Singleton dictionary for users by Farseen Ashraf"""

from decimal import Decimal
from reports import Reports
from wallets import Wallets


class Users:
    """A singleton dictionary for users"""
    _users: dict[str, dict[str, str]] = {}

    def __new__(cls):
        return cls

    @classmethod
    def register_user(cls, new_user: dict[str, str]) -> str:
        """register a user """
        if not new_user["user_name"] in cls._users:
            # generate really complicated unique user_id
            # using the existing user_name as the id for simplicity
            user_id = new_user["user_name"]
            cls._users[user_id] = new_user
            Reports.log_event(f"New user '{user_id}' created")
            # Create a wallet for the new user
            Wallets().create_wallet(user_id=user_id)
            # Give the user a sign up bonus
            Reports.log_event(f"Give new user '{user_id}' sign up bonus of 10")
            Wallets().adjust_balance(user_id=user_id, amount=Decimal(10))
            return user_id
        return ""

    @classmethod
    def edit_user(cls, user_id: str, user: dict) -> bool:
        """Do nothing"""
        print(user)
        print(user_id)
        return False

    @classmethod
    def change_pwd(cls, user_id: str, pwd: str) -> bool:
        """Do nothing"""
        print(user_id)
        print(pwd)
        return False
