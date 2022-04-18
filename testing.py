import pytest

from main import absolute


def test_absolute():
    assert absolute(5, 6) > 0

def test_number():
    assert -2 < 0
