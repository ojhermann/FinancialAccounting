import unittest
from datetime import datetime

from financial_accounting.main.accounts.account import Asset, Liability
from financial_accounting.main.entries.entry import Debit, Credit

key: str = 'key'
value: float = 3.14
date: datetime = datetime.now()

debit: Debit = Debit(account=Asset, key=key, value=value, date=date)

credit: Credit = Credit(account=Liability, key=key, value=value, date=date)


class TestDebit(unittest.TestCase):
    def testItCanGetAccount(self):
        self.assertEqual(
            Asset,
            debit.getAccount())

    def testItCanGetDate(self):
        self.assertEqual(
            date,
            debit.getDate())

    def testItCanGetKey(self):
        self.assertEqual(
            key,
            debit.getKey())

    def testItCanGetType(self):
        self.assertEqual(
            Debit.__name__,
            debit.getType())

    def testItCanGetValue(self):
        self.assertEqual(
            value,
            debit.getValue())

    def testItCanRaiseValueError(self):
        self.assertRaises(
            ValueError,
            Debit,
            account=Asset,
            key=key,
            value=value * -1,
            date=date)


class TestCredit(unittest.TestCase):
    def testItCanGetAccount(self):
        self.assertEqual(
            Liability,
            credit.getAccount())

    def testItCanGetDate(self):
        self.assertEqual(
            date,
            credit.getDate())

    def testItCanGetKey(self):
        self.assertEqual(
            key,
            credit.getKey())

    def testItCanGetType(self):
        self.assertEqual(
            Credit.__name__,
            credit.getType())

    def testItCanGetValue(self):
        self.assertEqual(
            value,
            credit.getValue())

    def testItCanRaiseValueError(self):
        self.assertRaises(
            ValueError,
            Credit,
            account=Liability,
            key=key,
            value=value * -1,
            date=date)


if __name__ == '__main__':
    unittest.main()
