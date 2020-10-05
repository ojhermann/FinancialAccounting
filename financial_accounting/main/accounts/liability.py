from financial_accounting.main.accounts.account import Account


class Liability(Account):
    @staticmethod
    def is_liability() -> bool:
        return True
