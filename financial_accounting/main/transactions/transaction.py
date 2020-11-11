from typing import Union, List

from financial_accounting.main.entries.credit import Credit
from financial_accounting.main.entries.debit import Debit
from financial_accounting.main.transactions.identifier import Identifier


class Transaction:
    def __init__(self, identifier: Identifier):
        self.__id: Identifier = identifier
        self.__debits: List[Debit] = list()
        self.__credits: List[Credit] = list()

    def get_identifier(self) -> Identifier:
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

    def is_valid(self) -> bool:
        if not self.__debits or not self.__credits:
            return False

        return self.is_balanced()

    def get_journal_entry(self) -> str:
        entries: List[Union[Debit, Credit]] = self.get_debits() + self.get_credits()
        max_width: int = max([len(entry.get_account().get_name()) for entry in entries]) + len("Dr. \t")

        result: str = f'{self.get_identifier()}\n'

        for debit in self.get_debits():
            representation: str = f'Dr. {debit.get_account().get_name()}'
            spaces: str = ' ' * (max_width - len(debit.get_account().get_name()))
            representation += spaces
            representation += f'\t{str(debit.get_value())}'
            result += f'{representation}\n'

        for credit in self.get_credits():
            representation: str = f'\tCr. {credit.get_account().get_name()}'
            spaces: str = ' ' * (max_width - len(credit.get_account().get_name()))
            representation += spaces
            representation += f'\t{str(credit.get_value())}'
            result += f'{representation}\n'

        return result
