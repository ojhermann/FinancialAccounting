from bisect import bisect_right
from typing import List, Union

from financial_accounting.main.entries.entry import Credit, Debit


class Transaction:
    def __init__(self,
                 identifier: str):
        self.__identifier: str = identifier
        self.__credits: List[Credit] = list()
        self.__debits: List[Debit] = list()

    def __repr__(self) -> str:
        return f'{self.get_identifier()}\n{self.get_debits()}\n{self.get_credits()}'

    def __add(self,
              entry: Union[Debit, Credit],
              entries: List[Union[Debit, Credit]]) -> None:
        if not entries:
            entries.append(entry)
        else:
            insert_index: int = bisect_right(entries, entry)
            if entries[insert_index - 1] == entry:
                raise ValueError(f'{entry} is already recorded in {self.get_identifier()}')
            else:
                entries.insert(insert_index, entry)

    def add(self,
            entry: Union[Debit, Credit]) -> bool:
        if isinstance(entry, Credit):
            self.__add(entry=entry, entries=self.__credits)
            return True

        if isinstance(entry, Debit):
            self.__add(entry=entry, entries=self.__debits)
            return True

        raise TypeError('Only a Credit or Debit can be added to a Transaction')

    def get_identifier(self) -> str:
        return self.__identifier

    def get_credits(self) -> List[Credit]:
        return self.__credits

    def get_debits(self) -> List[Debit]:
        return self.__debits

    def get_credit_balance(self) -> float:
        return sum(credit.get_value() for credit in self.get_credits())

    def get_debit_balance(self) -> float:
        return sum(debit.get_value() for debit in self.get_debits())

    def is_balanced(self) -> bool:
        return self.get_debit_balance() == self.get_credit_balance()
