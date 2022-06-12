import math

import pytest


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


@pytest.mark.check
def testsquare():
    num = 7
    assert num * 7 == 40


def tesequality():
    assert 10 == 11
