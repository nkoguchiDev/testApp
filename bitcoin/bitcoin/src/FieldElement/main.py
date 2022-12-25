class FieldElement:
    def __init__(self, num, prime) -> None:
        if num >= prime or num < 0:
            error = f"Num {num} not in field range 0 to {prime}"
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self) -> str:
        return f"FieldElement _{self.prime}({self.num})"

    def __eq__(self, __o: object) -> bool:
        if __o is None:
            return False
        return self.num == __o.num and self.prime == __o.prime

    def __ne__(self, __o: object) -> bool:
        return not (self == __o)
