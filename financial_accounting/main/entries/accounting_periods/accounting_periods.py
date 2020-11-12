class AccountingPeriod(str):
    def __init__(self, value: str):
        super().__init__()
        if not isinstance(value, str):
            raise TypeError("AccountingPeriod values must be str")
        if not value.strip():
            raise ValueError("AccountingPeriod values cannot be blank")
        self.__value: str = value

    def __new__(cls, value: str):
        return str.__new__(cls, value)


class AccountingPeriods:
    Q1: AccountingPeriod = AccountingPeriod(value="Q1")
    Q2: AccountingPeriod = AccountingPeriod(value="Q2")
    Q3: AccountingPeriod = AccountingPeriod(value="Q3")
    Q4: AccountingPeriod = AccountingPeriod(value="Q4")
