import string

from sympy import Symbol, sieve, expand, factor
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

    @property
    def pow(self):
        return self.a ** self.b


class Calcv2:
    def __init__(self) -> None:
        self.result = 0

    def add(self, input):
        self.result += self._check_input_type(input)

    def sub(self, input):
        self.result -= self._check_input_type(input)

    def mul(self, input):
        self.result *= self._check_input_type(input)

    def div(self, input):
        self.result /= self._check_input_type(input)

    def pow(self, input):
        self.result **= self._check_input_type(input)

    @property
    def expand(self):
        return expand(self.result)

    @property
    def factor(self):
        return factor(self.result)

    def reset(self):
        self.result = 0

    def _check_input_type(self, value):
        if isinstance(value, str):
            return Symbol(value)
        if isinstance(value, int):
            return float(value)
        raise TypeError("support type is str or int")


def is_prime_number(n: int) -> bool:
    return n in sieve


def prime_factorize(n: int) -> dict:
    return factorint(n)


def main():
    c = Calcv2()
    c.add("x")
    c.add(2)
    c.mul(2)
    print(c.expand)


if __name__ == "__main__":
    main()
