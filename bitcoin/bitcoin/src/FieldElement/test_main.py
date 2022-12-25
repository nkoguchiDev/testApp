from main import FieldElement


def test_main():
    a = FieldElement(7, 13)
    b = FieldElement(6, 13)

    assert (a == b) is False
    assert (a == a) is True

    assert (a != b) is True
    assert (a != a) is False
