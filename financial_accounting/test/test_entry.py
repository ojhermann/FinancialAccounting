import unittest
from datetime import datetime

from financial_accounting.main.account import Account
from financial_accounting.main.entries import Entry

key: str = 'key'

type: str = 'Entry'

value: float = 3.14

date: datetime = datetime.now()

entry: Entry = Entry(account=Account, key=key, value=value, date=date)


class TestEntry(unittest.TestCase):

    def testItCanGetAccount(self):
        self.assertEqual(
            entry.getAccount(),
            Account)

    def testItCanGetDate(self):
        self.assertEqual(
            entry.getDate(),
            date)

    def testItCanGetKey(self):
        self.assertEqual(
            entry.getKey(),
            key)

    def testItCanGetType(self):
        self.assertEqual(
            entry.getType(),
            type)

    def testItCanGetValue(self):
        self.assertEqual(
            entry.getValue(),
            value)

    def testItCanRaiseValueError(self):
        self.assertRaises(
            ValueError,
            Entry,
            account=Account,
            key=key,
            value=value * -1,
            date=date)


if __name__ == '__main__':
    unittest.main()
