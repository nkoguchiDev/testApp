from main import splitter

from hypothesis import given
from hypothesis.strategies import integers


@given(integers())
def test_main(s):
    li = range(s)
    splitter(li)
