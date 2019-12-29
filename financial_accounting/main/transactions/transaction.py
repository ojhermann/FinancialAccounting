from typing import Dict, Union, Type
from financial_accounting.main.entries.entry import Entry, Debit, Credit

acceptableTypes: Union = Union[Credit, Debit]


class Transaction:
    def __init__(self):
        self.__entries: Dict[str, acceptableTypes] = dict()

    @staticmethod
    def __createKey(entry: Entry) -> str:
        return entry.getType() + entry.getKey()

    def __getEntries(self,
                     entryType: Type[Entry]) -> Dict[str, acceptableTypes]:
        return {entryKey: entry for (entryKey, entry) in self.__entries.items() if type(entry) == entryType}

    def __getBalance(self,
                     entryType: Type[Entry]):
        return sum([entry.getValue() for entry in self.__getEntries(entryType).values()])

    def add(self,
            entry: acceptableTypes) -> None:
        if type(entry) not in acceptableTypes.__args__:
            raise TypeError('Only Debits and Credits can be added to a TransactionDict')

        transactionKey: str = self.__createKey(entry)

        if transactionKey in self.getEntries():
            entryType: str = entry.getType()
            accountType: str = entry.getAccount().getType()
            accountName: str = entry.getAccount().getName()
            raise ValueError(f'{entryType} for {accountType} {accountName} is already recorded.')

        self.__entries[transactionKey] = entry

    def getCredits(self) -> Dict[str, Credit]:
        return self.__getEntries(Credit)

    def getCreditBalance(self):
        return self.__getBalance(Credit)

    def getDebits(self) -> Dict[str, Debit]:
        return self.__getEntries(Debit)

    def getDebitBalance(self):
        return self.__getBalance(Debit)

    def getEntries(self) -> Dict[str, acceptableTypes]:
        return self.__entries

    def isBalanced(self):
        return self.getDebitBalance() == self.getCreditBalance()
