
class Point:
    def __init__(self, x, y, a, b) -> None:
        self.a = a
        self.b = b
        self.x = x
        self.y = y

        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError(f"({x}, {y}) is not on the curve.")

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y \
            and self.a == __o.a and self.b == __o.b

    def __ne__(self, __o: object) -> bool:
        return not self == __o


if __name__ == "__main__":
    p = Point(5, 7, 5, 7)
