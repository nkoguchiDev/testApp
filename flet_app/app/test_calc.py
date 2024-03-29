from calc import Calc


def test01():
    calc_src = ["1", "+", "2", "-", "3"]
    c = Calc(calc_src)
    assert c.result == "0"


def test02():
    calc_src = ["1", "+", "2", "/", "3"]
    c = Calc(calc_src)
    assert c.result == "1.0"


def test03():
    calc_src = ["x", "+", "2", "*", "3"]
    c = Calc(calc_src)
    assert c.expand == "3*(x+2)"
