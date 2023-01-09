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

    def __add__(self, __o: object) -> object:
        if self.prime != __o.prime:
            raise TypeError("Cannot add two numbers in differrent Fields")
        num = (self.num + __o.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, __o: object) -> object:
        if self.prime != __o.prime:
            raise TypeError("Cannot subtract two numbers in differrent Fields")

        """
        self.num and other.num are the actual value
        self.prime is what we need to mod against
        pythonにおける整数の割り算の結果は常に負の無限大の方向に丸められる
        参考<https://rseiub.com/59>
        """
        num = (self.num - __o.num) % self.prime
        # we return an element of the same class
        return self.__class__(num, self.prime)

    def __mul__(self, __o: object) -> object:
        if self.prime != __o.prime:
            raise TypeError("Cannot multiply two numbers in differrent Fields")

        num = (self.num * __o.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent: int) -> object:
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, __o):
        if self.prime != __o.prime:
            raise TypeError("Cannot divide two nombers in different Fields")
        """
        use Fermat's little theorm:
        self.num**(p-1) % p == 1
        this means:
        1/n == pow(n, p-1, p)
        we return an element of the same class
        """
        num = self.num * pow(__o.num, self.prime - 2, self.prime) % self.prime
        return self.__class__(num, self.prime)
