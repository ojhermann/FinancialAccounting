import unittest
from datetime import datetime

from financial_accounting.main.accounts import Account
from financial_accounting.main.entry import Entry

accountName: str = 'assetName'
account: Account = Account(name=accountName)

key: str = 'key'

type: str = 'Entry'

value: float = 3.14

date: datetime = datetime.now()

entry: Entry = Entry(account=account, key=key, value=value, date=date)


class TestEntry(unittest.TestCase):

    def testItCanGetAccount(self):
        self.assertEqual(
            entry.getAccount(),
            account)

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
            account=account,
            key=key,
            value=value * -1,
            date=date)


if __name__ == '__main__':
    unittest.main()
