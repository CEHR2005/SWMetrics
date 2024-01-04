# Ticket 6
import math

import pytest
from math_functions import custom_round


def test_floor_standard_positive():
    assert custom_round(3.7) == 3


def test_floor_standard_negative():
    assert custom_round(-3.7) == -4


def test_floor_whole_number():
    assert custom_round(5) == 5


def test_floor_zero():
    assert custom_round(0) == 0


def test_floor_small_fraction():
    assert custom_round(4.9999) == 4


def test_floor_negative_fraction_close_to_whole():
    assert custom_round(-3.0001) == -4


def test_floor_large_number():
    assert custom_round(123456789.123) == 123456789


def test_floor_very_small_negative():
    assert custom_round(-0.0001) == -1


def test_floor_float_no_fractional_part():
    assert custom_round(7.0) == 7


def test_floor_infinity():
    with pytest.raises(OverflowError):
        math.floor(float('inf'))


def test_floor_negative_infinity():
    with pytest.raises(OverflowError):
        math.floor(float('-inf'))


def test_floor_nan():
    with pytest.raises(ValueError):
        math.floor(float('nan'))
