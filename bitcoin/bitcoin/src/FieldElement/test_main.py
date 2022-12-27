from main import FieldElement


def test_eq():
    a = FieldElement(7, 13)
    b = FieldElement(6, 13)

    assert (a == b) is False
    assert (a == a) is True

    assert (a != b) is True
    assert (a != a) is False


def test_ne():
    a = FieldElement(7, 13)
    b = FieldElement(6, 13)

    assert (a != b) is True
    assert (a != a) is False


def test_add():
    a = FieldElement(7, 13)
    b = FieldElement(12, 13)
    c = FieldElement(6, 13)

    assert ((a + b) == c) is True


def test_sub():
    a = FieldElement(6, 19)
    b = FieldElement(13, 19)
    c = FieldElement(12, 19)

    assert ((a - b) == c) is True


def test_mul():
    a = FieldElement(3, 13)
    b = FieldElement(12, 13)
    c = FieldElement(10, 13)
    assert ((a * b) == c) is True


def test_pow():
    a = FieldElement(3, 13)
    b = FieldElement(1, 13)
    assert ((a ** 3) == b) is True
