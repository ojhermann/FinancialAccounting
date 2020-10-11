from datetime import datetime
from typing import Type

from financial_accounting.main.accounts.account import Account


class Entry:
    def __init__(self, account_type: Type[Account], unit: str, value: int, year: int, month: int, day: int):
        self.__account: Type[Account] = account_type
        self.__unit: str = unit
        self.__value: int = self._get_value(value)
        self.__date: datetime = datetime(year=year, month=month, day=day)

    def __repr__(self) -> str:
        return self.__class__.__name__

    def __str__(self) -> str:
        return self.__repr__()

    @staticmethod
    def _get_value(value: int) -> int:
        if not isinstance(value, int):
            raise TypeError(f"value must be an int: given value {value} is not an int")

        if value < 0:
            raise ValueError(f"value must be positive: given value {value} < 0")
        return value

    @staticmethod
    def is_debit() -> bool:
        return False

    @staticmethod
    def is_credit() -> bool:
        return False

    def get_account(self) -> Type[Account]:
        return self.__account

    def get_unit(self) -> str:
        return self.__unit

    def get_value(self) -> int:
        return self.__value

    def get_date(self) -> datetime:
        return self.__date
