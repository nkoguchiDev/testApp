import string

from sympy import Symbol, sieve, expand, factor
from sympy.ntheory import factorint


class Calc:
    def __init__(self, inputs: list) -> None:
        self.calc_src = inputs

    def _add(self, operand1, operand2):
        return check_value(operand1) + check_value(operand2)

    def _sub(self, operand1, operand2):
        return check_value(operand1) - check_value(operand2)

    def _mul(self, operand1, operand2):
        return check_value(operand1) * check_value(operand2)

    def _div(self, operand1, operand2):
        return check_value(operand1) / check_value(operand2)

    def _pow(self, operand1, operand2):
        return check_value(operand1) ** check_value(operand2)

    @property
    def expand(self):
        return expand(self.result)

    @property
    def factor(self):
        return factor(self.result)

    @property
    def result(self):
        # merge int value
        operand1 = ""
        operand2 = ""
        operator = None
        for value in self.calc_src:
            if value in ("1",
                         "2",
                         "3",
                         "4",
                         "5",
                         "6",
                         "7",
                         "8",
                         "9",
                         "0",
                         ".",
                         "x",
                         "y",
                         "z"):
                if operator is None:
                    operand1 = f"{operand1}{value}"
                    continue
                else:
                    operand2 = f"{operand2}{value}"
                    continue
            elif value in ("+", "-", "*", "/", "^"):
                if operator is None:
                    operator = value
                    continue
                if operand2 == "":
                    operator = value
                    continue
                else:
                    operand1 = self.condition(
                        int(operand1), int(operand2), operator)
                    operand2 = ""
                    operator = value
        operand1 = self.condition(int(operand1), int(operand2), operator)
        return operand1

    def condition(self, operand1, operand2, operator):
        print(operand1, operand2, operator)
        result = None
        if operator == "+":
            result = self._add(operand1, operand2)

        elif operator == "-":
            result = self._sub(operand1, operand2)

        elif operator == "*":
            result = self._mul(operand1, operand2)

        elif operator == "/":
            result = self._div(operand1, operand2)

        elif operator == "^":
            result = self._pow(operand1, operand2)
        return str(result)

    def reset(self):
        self.result = 0


def check_value(value):
    if isinstance(value, str):
        return Symbol(value)
    if isinstance(value, int):
        return int(value)
    raise TypeError("support type is str or int")


def is_prime_number(n: int) -> bool:
    return n in sieve


def prime_factorize(n: int) -> dict:
    return factorint(n)


def main():
    print(Symbol("1") + Symbol("1"))


if __name__ == "__main__":
    main()
