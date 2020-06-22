from __future__ import annotations

from datetime import datetime
from typing import Tuple

from financial_accounting.main.accounts.account import Account


class Entry:
    def __init__(self,
                 account: Account,
                 identifier: str,
                 currency: str,
                 value: float,
                 date: datetime = datetime.utcnow()):
        if value < 0:
            raise ValueError('All values must be positive')
        self.__account: Account = account
        self.__identifier: str = identifier
        self.__currency: str = currency
        self.__value: float = value
        self.__date: datetime = date

    @staticmethod
    def __get_equality_elements(entry: Entry) -> Tuple[datetime, Account, str, str, float]:
        return entry.get_date(), entry.get_account(), entry.get_identifier(), entry.get_currency(), entry.get_value()

    def __lt__(self,
               other: Entry) -> bool:
        return self.__get_equality_elements(self) < self.__get_equality_elements(other)

    def __eq__(self,
               other: Entry) -> bool:
        return self.__get_equality_elements(self) == self.__get_equality_elements(other)

    def __gt__(self,
               other: Entry) -> bool:
        return self.__get_equality_elements(self) > self.__get_equality_elements(other)

    def __repr__(self) -> str:
        return f'({self.__class__.__name__}, ' \
               f'{self.get_account()}, ' \
               f'{self.get_identifier()}, ' \
               f'{self.get_currency()}, ' \
               f'{self.get_value()}, ' \
               f'{self.get_date()})'

    def get_account(self) -> Account:
        return self.__account

    def get_identifier(self) -> str:
        return self.__identifier

    def get_currency(self) -> str:
        return self.__currency

    def get_date(self) -> datetime:
        return self.__date

    def get_value(self) -> float:
        return self.__value


class Credit(Entry):
    def __init__(self,
                 account: Account,
                 identifier: str,
                 currency: str,
                 value: float,
                 date: datetime = datetime.utcnow()):
        super().__init__(account, identifier, currency, value, date)


class Debit(Entry):
    def __init__(self,
                 account: Account,
                 identifier: str,
                 currency: str,
                 value: float,
                 date: datetime = datetime.utcnow()):
        super().__init__(account, identifier, currency, value, date)
