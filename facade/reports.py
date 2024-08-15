"""A singleton dictionary of reported events"""
import time


class Reports:
    """A Singleton dictionary of reported events"""
    """create a new protected variable called reports with a type hint of keys as int and 
    values as tuples"""
    _reports: dict[int, tuple[float, str]] = {}
    _row_id = 0

    def __new__(cls):
        return cls

    @classmethod
    def get_history(cls) -> dict:
        """A method to retrieve all historical events"""
        return cls._reports

    @classmethod
    def log_event(cls, event: str) -> bool:
        """method to add a new event to the record"""
        cls._reports[cls._row_id] = (time.time(), event)
        cls._row_id += 1
        return True
