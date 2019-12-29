import unittest
from datetime import datetime
from typing import List, Union

from financial_accounting.main.accounts.account import Asset, Liability
from financial_accounting.main.entries.entry import Debit, Credit
from financial_accounting.main.transactions.transaction import Transaction

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

transactionUnbalanced: Transaction = Transaction()
transactionUnbalanced.add(debitOne)
transactionUnbalanced.add(creditOne)

transactionBalanced: Transaction = Transaction()
transactionBalanced.add(debitOne)
transactionBalanced.add(debitTwo)
transactionBalanced.add(creditOne)


class TestUnbalancedTransaction(unittest.TestCase):
    def testItCanGetCredits(self):
        expectedEntries: List[Credit] = [creditOne]

        actualEntries: List[Credit] = list(transactionUnbalanced.getCredits().values())

        self.assertEqual(len(expectedEntries),
                         len(actualEntries))

        for entry in expectedEntries:
            self.assert_(actualEntries.__contains__(entry))

    def testItCanGetCreditBalance(self):
        self.assertEqual(valueCreditOne,
                         transactionUnbalanced.getCreditBalance())

    def testItCanGetDebits(self):
        expectedEntries: List[Debit] = [debitOne]

        actualEntries: List[Debit] = list(transactionUnbalanced.getDebits().values())

        self.assertEqual(len(expectedEntries),
                         len(actualEntries))

        for entry in expectedEntries:
            self.assert_(actualEntries.__contains__(entry))

    def testItCanGetDebitBalance(self):
        self.assertEqual(valueDebitOne,
                         transactionUnbalanced.getDebitBalance())

    def testItCanGetEntries(self):
        expectedEntries: List[Union[Credit, Debit]] = [creditOne, debitOne]

        actualEntries: List[Union[Credit, Debit]] = list(transactionUnbalanced.getEntries().values())

        self.assertEqual(len(expectedEntries),
                         len(actualEntries))

        for entry in expectedEntries:
            self.assert_(actualEntries.__contains__(entry))

    def testItCanCheckBalance(self):
        self.assertEqual(False,
                         transactionUnbalanced.isBalanced())


class TestBalancedTransaction(unittest.TestCase):
    def testItCanGetCredits(self):
        expectedEntries: List[Credit] = [creditOne]

        actualEntries: List[Credit] = list(transactionBalanced.getCredits().values())

        self.assertEqual(len(expectedEntries),
                         len(actualEntries))

        for entry in expectedEntries:
            self.assert_(actualEntries.__contains__(entry))

    def testItCanGetCreditBalance(self):
        self.assertEqual(valueCreditOne,
                         transactionBalanced.getCreditBalance())

    def testItCanGetDebits(self):
        expectedEntries: List[Debit] = [debitOne, debitTwo]

        actualEntries: List[Debit] = list(transactionBalanced.getDebits().values())

        self.assertEqual(len(expectedEntries),
                         len(actualEntries))

        for entry in expectedEntries:
            self.assert_(actualEntries.__contains__(entry))

    def testItCanGetDebitBalance(self):
        self.assertEqual(valueDebitOne + valueDebitTwo,
                         transactionBalanced.getDebitBalance())

    def testItCanGetEntries(self):
        expectedEntries: List[Union[Credit, Debit]] = [creditOne, debitOne, debitTwo]

        actualEntries: List[Union[Credit, Debit]] = list(transactionBalanced.getEntries().values())

        self.assertEqual(len(expectedEntries),
                         len(actualEntries))

        for entry in expectedEntries:
            self.assert_(actualEntries.__contains__(entry))

    def testItCanCheckBalance(self):
        self.assertEqual(True,
                         transactionBalanced.isBalanced())


class TestAddMethodErrors(unittest.TestCase):
    def testItCanRaiseTypeError(self):
        self.assertRaises(TypeError,
                          transactionBalanced.add,
                          'notTheCorrectType')

    def testItCanRaiseValueError(self):
        self.assertRaises(ValueError,
                          transactionBalanced.add,
                          debitOne)


if __name__ == '__main__':
    unittest.main()
