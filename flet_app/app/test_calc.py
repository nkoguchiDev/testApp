from calc import Calc


def test01():
    calc_src = ["1", "+", "1"]
    c = Calc(calc_src)
    assert c.result == "2"
