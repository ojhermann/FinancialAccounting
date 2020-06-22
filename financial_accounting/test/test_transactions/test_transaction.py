import unittest
from datetime import datetime

from financial_accounting.main.accounts.account import Asset, Liability, Equity
from financial_accounting.main.entries.entry import Credit, Debit
from financial_accounting.main.transactions.transaction import Transaction

asset: Asset = Asset()
liability: Liability = Liability()

d_one_id: str = 'd_one_id'
d_one_currency: str = 'USD'
d_one_value: float = 1.0
d_one_date: datetime = datetime.utcnow()
d_one: Debit = Debit(account=asset,
                     identifier=d_one_id,
                     currency=d_one_currency,
                     value=d_one_value,
                     date=d_one_date)

d_two_id: str = 'd_two_id'
d_two_currency: str = 'USD'
d_two_value: float = 2.0
d_two_date: datetime = datetime.utcnow()
d_two: Debit = Debit(account=asset,
                     identifier=d_two_id,
                     currency=d_two_currency,
                     value=d_two_value,
                     date=d_two_date)

d_three_id: str = 'd_three_id'
d_three_currency: str = 'USD'
d_three_value: float = 3.0
d_three_date: datetime = datetime.utcnow()
d_three: Debit = Debit(account=asset,
                       identifier=d_three_id,
                       currency=d_three_currency,
                       value=d_three_value,
                       date=d_three_date)

d_balance: float = d_one_value + d_two_value + d_three_value

c_one_id: str = 'c_one_id'
c_one_currency: str = 'USD'
c_one_value: float = 1.0
c_one_date: datetime = datetime.utcnow()
c_one: Credit = Credit(account=asset,
                       identifier=c_one_id,
                       currency=c_one_currency,
                       value=c_one_value,
                       date=c_one_date)

c_two_id: str = 'c_two_id'
c_two_currency: str = 'USD'
c_two_value: float = 2.0
c_two_date: datetime = datetime.utcnow()
c_two: Credit = Credit(account=asset,
                       identifier=c_two_id,
                       currency=c_two_currency,
                       value=c_two_value,
                       date=c_two_date)

c_three_id: str = 'c_three_id'
c_three_currency: str = 'USD'
c_three_value: float = 3.0
c_three_date: datetime = datetime.utcnow()
c_three: Credit = Credit(account=asset,
                         identifier=c_three_id,
                         currency=c_three_currency,
                         value=c_three_value,
                         date=c_three_date)

c_balance: float = c_one_value + c_two_value + c_three_value

transaction_id: str = 'transaction_id'
transaction: Transaction = Transaction(identifier=transaction_id)

transaction_id_unbalanced: str = 'transaction_id_unbalanced'
transaction_unbalanced: Transaction = Transaction(transaction_id_unbalanced)


class TestTransaction(unittest.TestCase):
    def test_it_an_add(self):
        # adding in reverse order
        self.assertTrue(transaction.add(d_three))
        self.assertTrue(transaction.add(d_two))
        self.assertTrue(transaction.add(d_one))
        self.assertTrue(transaction.add(c_three))
        self.assertTrue(transaction.add(c_two))
        self.assertTrue(transaction.add(c_one))

        # check order is correct
        for i in range(len(transaction.get_debits()) - 1):
            self.assertTrue(transaction.get_debits()[i] < transaction.get_debits()[i + 1])
        for i in range(len(transaction.get_credits()) - 1):
            self.assertTrue(transaction.get_credits()[i] < transaction.get_credits()[i + 1])

        # check that duplicates cannot be added
        self.assertRaises(ValueError, transaction.add, d_one)
        self.assertRaises(ValueError, transaction.add, c_one)

        # check that only Credits and Debits can be added
        self.assertRaises(TypeError, transaction.add, 'This should not work')
        self.assertRaises(TypeError, transaction.add, 1.3)

    def test_it_can_get_identifier(self):
        self.assertEqual(transaction_id,
                         transaction.get_identifier())

    def test_it_can_get_credits(self):
        self.assertEqual([c_one, c_two, c_three],
                         transaction.get_credits())

    def test_it_can_get_debits(self):
        self.assertEqual([d_one, d_two, d_three],
                         transaction.get_debits())

    def test_it_can_get_credit_balance(self):
        self.assertEqual(d_balance,
                         transaction.get_debit_balance())

    def test_it_can_get_debit_balance(self):
        self.assertEqual(c_balance,
                         transaction.get_credit_balance())

    def test_it_can_check_if_balanced(self):
        # check balanced transaction
        self.assertTrue(transaction.is_balanced())

        # check unbalanced transaction
        transaction_unbalanced.add(d_one)  # add a Debit with value 1.0
        self.assertFalse(transaction_unbalanced.is_balanced())
        transaction_unbalanced.add(c_two)  # add a Credit with value 2.0
        self.assertFalse(transaction_unbalanced.is_balanced())


if __name__ == '__main__':
    unittest.main()
