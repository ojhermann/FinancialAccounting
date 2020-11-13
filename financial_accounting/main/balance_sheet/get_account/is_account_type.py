from typing import Type, Union

from financial_accounting.main.accounts.asset import Asset
from financial_accounting.main.accounts.equity import Equity
from financial_accounting.main.accounts.liability import Liability
from financial_accounting.main.balance_sheet.get_account.exceptions import InvalidAccountType, NotDebitOrCredit
from financial_accounting.main.entries.credit import Credit
from financial_accounting.main.entries.debit import Debit


def is_account_type(entry: Union[Debit, Credit],
                    account_type: Union[Type[Asset], Union[Type[Liability], Type[Equity]]]):
    if not isinstance(entry, Debit) and not isinstance(entry, Credit):
        raise NotDebitOrCredit(attempted_entry=entry)

    if account_type is Asset:
        return entry.get_account().is_asset()
    elif account_type is Liability:
        return entry.get_account().is_liability()
    elif account_type is Equity:
        return entry.get_account().is_equity()
    else:
        raise InvalidAccountType(attempted_type=account_type)
