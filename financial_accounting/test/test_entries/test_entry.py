import unittest
from datetime import datetime

from financial_accounting.main.accounts.account import Account, Asset
from financial_accounting.main.entries.entry import Entry, Debit, Credit

key: str = 'key'
value: float = 3.14
date: datetime = datetime.now()

entry: Entry = Entry(account=Account, key=key, value=value, date=date)

debit: Entry = Debit(account=Asset, key=key, value=value, date=date)


class TestEntry(unittest.TestCase):
    def testItCanGetAccount(self):
        self.assertEqual(
            Account,
            entry.getAccount())

    def testItCanGetDate(self):
        self.assertEqual(
            date,
            entry.getDate())

    def testItCanGetKey(self):
        self.assertEqual(
            key,
            entry.getKey())

    def testItCanGetType(self):
        self.assertEqual(
            Entry.__name__,
            entry.getType())

    def testItCanGetValue(self):
        self.assertEqual(
            value,
            entry.getValue())

    def testItCanRaiseValueError(self):
        self.assertRaises(
            ValueError,
            Entry,
            account=Account,
            key=key,
            value=value * -1,
            date=date)


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


if __name__ == '__main__':
    unittest.main()
