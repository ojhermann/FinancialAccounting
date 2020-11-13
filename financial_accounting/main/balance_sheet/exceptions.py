from financial_accounting.main.transactions.transaction import Transaction


class NotATransaction(TypeError):
    def __init__(self, attempted_transaction):
        self.__attempted_transaction = attempted_transaction

    def get_message(self) -> str:
        return f'{self.__attempted_transaction} is not a Transaction'


class DuplicateTransaction(Exception):
    def __init__(self, transaction: Transaction):
        self.__transaction: Transaction = transaction

    def get_transaction(self) -> Transaction:
        return self.__transaction

    def get_message(self) -> str:
        return f"{self.get_transaction().get_identifier()} is already in the balance sheet"


class InvalidTransaction(Exception):
    def __init__(self, transaction: Transaction):
        self.__transaction: Transaction = transaction

    def get_transaction(self) -> Transaction:
        return self.__transaction

    def get_message(self) -> str:
        return f"{self.get_transaction().get_identifier()} is not valid"
