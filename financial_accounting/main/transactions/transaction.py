from collections import OrderedDict
from typing import Union, Type
from typing import OrderedDict as OrderedDictType
from financial_accounting.main.entries.entry import Entry, Debit, Credit

acceptableTypes: Union = Union[Credit, Debit]


def createTransactionKey(entry: Entry) -> str:
    return entry.getType() + entry.getKey()


class Transaction:
    def __init__(self):
        self.__entries: OrderedDictType[str, acceptableTypes] = OrderedDict()

    def __getEntries(self,
                     entryType: Type[Entry]) -> OrderedDictType[str, acceptableTypes]:
        return OrderedDict(
            {entryKey: entry for (entryKey, entry) in self.__entries.items() if type(entry) == entryType})

    def __getBalance(self,
                     entryType: Type[Entry]):
        return sum([entry.getValue() for entry in self.__getEntries(entryType).values()])

    def add(self,
            entry: acceptableTypes) -> None:
        if type(entry) not in acceptableTypes.__args__:
            raise TypeError('Only Debits and Credits can be added to a TransactionDict')

        transactionKey: str = createTransactionKey(entry)

        if transactionKey in self.getEntries():
            entryType: str = entry.getType()
            accountType: str = entry.getAccount().getType()
            accountName: str = entry.getAccount().getName()
            raise ValueError(f'{entryType} for {accountType} {accountName} is already recorded.')

        self.__entries[transactionKey] = entry

    def getCredits(self) -> OrderedDictType[str, Credit]:
        return self.__getEntries(Credit)

    def getCreditBalance(self):
        return self.__getBalance(Credit)

    def getDebits(self) -> OrderedDictType[str, Debit]:
        return self.__getEntries(Debit)

    def getDebitBalance(self):
        return self.__getBalance(Debit)

    def getEntries(self) -> OrderedDictType[str, acceptableTypes]:
        return self.__entries

    def isBalanced(self):
        return self.getDebitBalance() == self.getCreditBalance()
