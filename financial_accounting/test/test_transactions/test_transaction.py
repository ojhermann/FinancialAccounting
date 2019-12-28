import unittest
from datetime import datetime

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
        self.assertEqual(1,
                         len(transactionUnbalanced.getCredits()))

        self.assertIn(creditOne,
                      transactionUnbalanced.getCredits().values())

    def testItCanGetCreditBalance(self):
        self.assertEqual(valueCreditOne,
                         transactionUnbalanced.getCreditBalance())

    def testItCanGetDebits(self):
        self.assertEqual(1,
                         len(transactionUnbalanced.getDebits()))

        self.assertIn(debitOne,
                      transactionUnbalanced.getDebits().values())

    def testItCanGetDebitBalance(self):
        self.assertEqual(valueDebitOne,
                         transactionUnbalanced.getDebitBalance())

    def testItCanGetEntries(self):
        self.assertEqual(2,
                         len(transactionUnbalanced.getEntries()))

        self.assertIn(creditOne,
                      transactionUnbalanced.getEntries().values())

        self.assertIn(debitOne,
                      transactionUnbalanced.getEntries().values())

    def testItCanCheckBalance(self):
        self.assertEqual(False,
                         transactionUnbalanced.isBalanced())


class TestBalancedTransaction(unittest.TestCase):
    def testItCanGetCredits(self):
        self.assertEqual(1,
                         len(transactionBalanced.getCredits()))

        self.assertIn(creditOne,
                      transactionBalanced.getCredits().values())

    def testItCanGetCreditBalance(self):
        self.assertEqual(valueCreditOne,
                         transactionBalanced.getCreditBalance())

    def testItCanGetDebits(self):
        self.assertEqual(2,
                         len(transactionBalanced.getDebits()))

        self.assertIn(debitOne,
                      transactionBalanced.getDebits().values())

        self.assertIn(debitTwo,
                      transactionBalanced.getDebits().values())

    def testItCanGetDebitBalance(self):
        self.assertEqual(valueDebitOne + valueDebitTwo,
                         transactionBalanced.getDebitBalance())

    def testItCanGetEntries(self):
        self.assertEqual(3,
                         len(transactionBalanced.getEntries()))

        self.assertIn(creditOne,
                      transactionBalanced.getEntries().values())

        self.assertIn(debitOne,
                      transactionBalanced.getEntries().values())

        self.assertIn(debitTwo,
                      transactionBalanced.getEntries().values())

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
