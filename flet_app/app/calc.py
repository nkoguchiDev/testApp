import string

from sympy import Symbol, sieve
from sympy.ntheory import factorint


def add(a, b) -> str:
    if isinstance(a, str):
        a = Symbol(a)

    if isinstance(b, str):
        b = Symbol(b)
    return a + b


def sub(a, b) -> str:
    if isinstance(a, str):
        a = Symbol(a)

    if isinstance(b, str):
        b = Symbol(b)
    return a - b


def mul(a, b) -> str:
    if isinstance(a, str):
        a = Symbol(a)

    if isinstance(b, str):
        b = Symbol(b)
    return a * b


def div(a, b) -> str:
    if isinstance(a, str):
        a = Symbol(a)

    if isinstance(b, str):
        b = Symbol(b)
    return a / b


def is_prime_number(n: int) -> bool:
    return n in sieve


def prime_factorize(n: int) -> dict:
    return factorint(n)


def main():
    print(is_prime_number(7))


if __name__ == "__main__":
    main()
