import string

from sympy import Symbol, sieve
from sympy.ntheory import factorint


class Calc:
    def __init__(self, a, b) -> None:
        if isinstance(a, str):
            self.a = Symbol(a)
        else:
            self.a = a

        if isinstance(b, str):
            self.b = Symbol(b)
        else:
            self.b = b

    @property
    def add(self):
        return self.a + self.b

    @property
    def sub(self):
        return self.a - self.b

    @property
    def mul(self):
        return self.a * self.b

    @property
    def div(self):
        return self.a / self.b


def is_prime_number(n: int) -> bool:
    return n in sieve


def prime_factorize(n: int) -> dict:
    return factorint(n)


def main():
    print(is_prime_number(7))


if __name__ == "__main__":
    main()
