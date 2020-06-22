class Account:
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}'


class Asset(Account):
    pass


class Liability(Account):
    pass


class Equity(Account):
    pass
