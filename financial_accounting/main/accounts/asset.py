from financial_accounting.main.accounts.account import Account


class Asset(Account):
    @staticmethod
    def is_asset() -> bool:
        return True
