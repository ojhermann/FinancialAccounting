from datetime import datetime
from typing import Type
from financial_accounting.main.accounts.account import Account


class Entry:
    def __init__(self,
                 account: Type[Account],
                 key: str,
                 value: float,
                 date: datetime = datetime.now()):
        self.__account: Type[Account] = account
        self.__key: str = key
        self.__value: float = setValue(value)
        self.__date: datetime = date

    def getAccount(self) -> Type[Account]:
        return self.__account

    def getDate(self) -> datetime:
        return self.__date

    def getKey(self) -> str:
        return self.__key

    def getType(self) -> str:
        return self.__class__.__name__

    def getValue(self) -> float:
        return self.__value


def setValue(value: float):
    if value < 0:
        raise ValueError('All values must be positive.')

    return value


class Debit(Entry):
    def __init__(self, account: Type[Account], key: str, value: float, date: datetime = datetime.now()):
        super().__init__(account, key, value, date)


class Credit(Entry):
    def __init__(self, account: Type[Account], key: str, value: float, date: datetime = datetime.now()):
        super().__init__(account, key, value, date)