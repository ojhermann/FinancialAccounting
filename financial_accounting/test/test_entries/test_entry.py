import unittest
from datetime import datetime

from financial_accounting.main.accounts.account import Asset, Liability
from financial_accounting.main.entries.entry import Entry


class TestEntry(unittest.TestCase):
    asset: Asset = Asset()
    liability: Liability = Liability()

    now: datetime = datetime.utcnow()
    later: datetime = datetime.utcnow()

    currency: str = 'USD'

    value: float = 1.0

    one_identifier: str = 'one'
    two_identifier: str = 'two'

    one: Entry = Entry(account=asset,
                       identifier=one_identifier,
                       currency=currency,
                       value=value,
                       date=now)
    two: Entry = Entry(account=liability,
                       identifier=two_identifier,
                       currency=currency,
                       value=value,
                       date=later)

    def test_it_can_raise_value_error(self) -> None:
        self.assertRaises(ValueError,
                          Entry,
                          TestEntry.asset,
                          TestEntry.one_identifier,
                          TestEntry.currency,
                          TestEntry.value * -1,
                          TestEntry.now)

    def test_it_can_get_account(self) -> None:
        self.assertTrue(isinstance(TestEntry.one.get_account(), Asset))
        self.assertTrue(isinstance(TestEntry.two.get_account(), Liability))

    def test_it_can_get_identifier(self) -> None:
        self.assertEqual(TestEntry.one_identifier, TestEntry.one.get_identifier())
        self.assertEqual(TestEntry.two_identifier, TestEntry.two.get_identifier())

    def test_it_can_get_currency(self) -> None:
        self.assertEqual(TestEntry.currency, TestEntry.one.get_currency())
        self.assertEqual(TestEntry.currency, TestEntry.two.get_currency())

    def test_it_can_get_date(self) -> None:
        self.assertEqual(TestEntry.now, TestEntry.one.get_date())
        self.assertEqual(TestEntry.later, TestEntry.two.get_date())

    def test_it_can_get_value(self) -> None:
        self.assertEqual(TestEntry.value, TestEntry.one.get_value())
        self.assertEqual(TestEntry.value, TestEntry.two.get_value())

    def test_lt_works(self) -> None:
        self.assertTrue(TestEntry.one < TestEntry.two)

    def test_gt_works(self) -> None:
        self.assertTrue(TestEntry.two > TestEntry.one)

    def test_eq_works(self) -> None:
        self.assertEqual(TestEntry.one, Entry(account=TestEntry.asset,
                                              identifier=TestEntry.one_identifier,
                                              currency=TestEntry.currency,
                                              value=TestEntry.value,
                                              date=TestEntry.now))


if __name__ == '__main__':
    unittest.main()
