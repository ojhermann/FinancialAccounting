from typing import List, Type, Dict, Union

from financial_accounting.main.accounts.asset import Asset
from financial_accounting.main.accounts.equity import Equity
from financial_accounting.main.accounts.liability import Liability
from financial_accounting.main.balance_sheet.get_account.is_account_type import is_account_type
from financial_accounting.main.entries.credit import Credit
from financial_accounting.main.entries.debit import Debit


class AccountDebitsAndCredits(dict):
    def __init__(self, debits: List[Debit], credits: List[Credit]):
        super().__init__()
        self['debits']: List[debits] = debits
        self['credits']: List[credits] = credits


def get_account(debits: List[Debit],
                credits: List[Credit],
                account_type: Union[Type[Asset], Union[Type[Liability], Type[Equity]]]) -> AccountDebitsAndCredits:
    return AccountDebitsAndCredits(
        debits=[debit for debit in debits if is_account_type(entry=debit, account_type=account_type)],
        credits=[credit for credit in credits if is_account_type(entry=credit, account_type=account_type)])
