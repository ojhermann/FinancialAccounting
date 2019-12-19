class AccountType:
    account: str = 'Account'
    asset: str = 'Asset'
    liability: str = 'Liability'
    equity: str = 'Equity'


class Account:
    @staticmethod
    def getType() -> str:
        return AccountType.account

    @classmethod
    def getName(cls) -> str:
        return cls.__name__


class Asset(Account):
    @staticmethod
    def getType() -> str:
        return AccountType.asset


class Liability(Account):
    @staticmethod
    def getType() -> str:
        return AccountType.liability


class Equity(Account):
    @staticmethod
    def getType() -> str:
        return AccountType.equity
