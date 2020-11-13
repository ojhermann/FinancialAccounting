from typing import Type


class InvalidAccountType(Exception):
    def __init__(self, attempted_type: Type):
        self.__attempted_type: Type = attempted_type

    def get_message(self) -> str:
        return f'Type {self.__attempted_type} is not permitted; only Asset, Liability, or Equity types are allowed'


class NotDebitOrCredit(TypeError):
    def __init__(self, attempted_entry):
        self.__attempted_entry = attempted_entry

    def get_message(self) -> str:
        return f'{self.__attempted_entry} is not permitted; only Debit or Credit objects are allowed'
