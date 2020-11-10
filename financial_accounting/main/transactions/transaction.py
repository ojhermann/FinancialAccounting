from typing import Union, List

from financial_accounting.main.entries.credit import Credit
from financial_accounting.main.entries.debit import Debit
from financial_accounting.main.transactions.identifier import Identifier


class Transaction:
    def __init__(self, identifier: Identifier):
        self.__id: Identifier = identifier
        self.__debits: List[Debit] = list()
        self.__credits: List[Credit] = list()

    def get_identifier(self) -> str:
        return self.__id

    def add(self, entry: Union[Debit, Credit]) -> None:
        if not isinstance(entry, (Debit, Credit)):
            raise TypeError("Only Debit and Credit objects can be added to a transaction")
        if entry.is_debit():
            self.__debits.append(entry)
        else:
            self.__credits.append(entry)

    def get_debits(self) -> List[Debit]:
        return self.__debits

    def get_credits(self) -> List[Credit]:
        return self.__credits

    def get_debit_total_value(self) -> int:
        return sum([debit.get_value() for debit in self.get_debits()])

    def get_credit_total_value(self) -> int:
        return sum([credit.get_value() for credit in self.get_credits()])

    def is_balanced(self) -> bool:
        return self.get_debit_total_value() == self.get_credit_total_value()
