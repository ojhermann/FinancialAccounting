import unittest
from collections import OrderedDict
from datetime import datetime
from typing import OrderedDict as OrderedDictType

from financial_accounting.main.accounts.account import Asset, Liability
from financial_accounting.main.entries.entry import Debit, Credit
from financial_accounting.main.transactions.transaction import Transaction, createTransactionKey, acceptableTypes

date: datetime = datetime.now()

keyDebitOne: str = 'keyDebitOne'
valueDebitOne: float = 3.14
debitOne: Debit = Debit(account=Asset, key=keyDebitOne, value=valueDebitOne, date=date)

keyDebitTwo: str = 'keyDebitTwo'
valueDebitTwo: float = 3.14
debitTwo: Debit = Debit(account=Asset, key=keyDebitTwo, value=valueDebitTwo, date=date)

keyCreditOne: str = 'keyCreditOne'
valueCreditOne: float = valueDebitOne + valueDebitTwo
creditOne: Credit = Credit(account=Liability, key=keyCreditOne, value=valueCreditOne, date=date)


class TestCreateKey(unittest.TestCase):
    def testItCanCreateTransactionKey(self):
        expectedTransactionKey: str = debitOne.getType() + debitOne.getKey()

        self.assertEqual(expectedTransactionKey,
                         createTransactionKey(debitOne))


class TestTransaction(unittest.TestCase):
    def testItCanAddAndGet(self):
        transaction: Transaction = Transaction()
        transaction.add(debitOne)
        transaction.add(creditOne)
        transaction.add(debitTwo)

        expectedEntries: OrderedDictType[str, acceptableTypes] = OrderedDict(
            {createTransactionKey(entry): entry for entry in [debitOne, creditOne, debitTwo]})
        self.assertEqual(expectedEntries,
                         transaction.getEntries())

        expectedDebits: OrderedDictType[str, Debit] = OrderedDict(
            {createTransactionKey(entry): entry for entry in [debitOne, debitTwo]})
        self.assertEqual(expectedDebits,
                         transaction.getDebits())
        self.assertEqual(valueDebitOne + valueDebitTwo,
                         transaction.getDebitBalance())

        expectedCredits: OrderedDictType[str, Credit] = OrderedDict(
            {createTransactionKey(entry): entry for entry in [creditOne]})
        self.assertEqual(expectedCredits,
                         transaction.getCredits())
        self.assertEqual(valueCreditOne,
                         transaction.getCreditBalance())

    def testItCanCheckBalance(self):
        transaction: Transaction = Transaction()
        transaction.add(debitOne)
        transaction.add(creditOne)

        self.assertEqual(False,
                         transaction.isBalanced())

        transaction.add(debitTwo)

        self.assertEqual(True,
                         transaction.isBalanced())

    def testItCanRaiseErrors(self):
        transaction: Transaction = Transaction()
        transaction.add(debitOne)

        self.assertRaises(TypeError,
                          transaction.add,
                          'notTheCorrectType')

        self.assertRaises(ValueError,
                          transaction.add,
                          debitOne)


if __name__ == '__main__':
    unittest.main()
