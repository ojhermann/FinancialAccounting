class Identifier(str):
    def __init__(self, value: str):
        super().__init__()
        if not isinstance(value, str):
            raise TypeError("Identifier values must be str")
        if not value.strip():
            raise ValueError("Identifier values cannot be blank")
        self.__value: str = value

    def __new__(cls, value: str):
        return str.__new__(cls, value)
