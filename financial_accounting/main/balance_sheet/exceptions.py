from financial_accounting.main.transactions.transaction import Transaction


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
