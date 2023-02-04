from calc import Calc


def test01():
    calc_src = ["1", "+", "2", "-", "3"]
    c = Calc(calc_src)
    assert c.result == "0"


def test02():
    calc_src = ["1", "+", "2", "/", "3"]
    c = Calc(calc_src)
    assert c.result == "1"
