from financial_accounting.main.accounts.account import Account


class Equity(Account):
    @staticmethod
    def is_equity() -> bool:
        return True
