import string

from sympy import Symbol
from sympy.ntheory import factorint


def main():
    calc = Calc(2, "x")
    print(calc.product)


class Calc:
    def __init__(self, x, y) -> None:
        if isinstance(x, str):
            self.x = Symbol(x)
        else:
            self.x = x

        if isinstance(y, str):
            self.y = Symbol(y)
        else:
            self.y = y

    @property
    def sum(self):
        return self.x + self.y

    @property
    def diff(self):
        return self.x - self.y

    @property
    def product(self):
        return self.x * self.y

    @property
    def quotient(self):
        return self.x / self.y


def is_prime_number(n: int) -> bool:
    if n in [0, 1]:
        return False

    if len(factorint(n)) == 1:
        return True
    else:
        return False


def prime_factorize(n: int) -> dict:
    return factorint(n)


if __name__ == "__main__":
    main()
