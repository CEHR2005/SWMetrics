# test_math_functions.py

"""
Module to test custom rounding functions.
"""

import math
import pytest
from math_functions import custom_round


def test_floor_standard_positive():
    """
    Test rounding up for a standard positive number.
    """
    assert custom_round(3.7) == 3


def test_floor_standard_negative():
    """
    Test rounding up for a standard negative number.
    """
    assert custom_round(-3.7) == -4


def test_floor_whole_number():
    """
    Test rounding up for a whole number.
    """
    assert custom_round(5) == 5


def test_floor_zero():
    """
    Test rounding up for zero.
    """
    assert custom_round(0) == 0


def test_floor_small_fraction():
    """
    Test rounding up for a number with a small fraction.
    """
    assert custom_round(4.9999) == 4


def test_floor_negative_fraction_close_to_whole():
    """
    Test rounding up for a negative number close to a whole number.
    """
    assert custom_round(-3.0001) == -4


def test_floor_large_number():
    """
    Test rounding up for a large number.
    """
    assert custom_round(123456789.123) == 123456789


def test_floor_very_small_negative():
    """
    Test rounding up for a very small negative number.
    """
    assert custom_round(-0.0001) == -1


def test_floor_float_no_fractional_part():
    """
    Test rounding up for a float number with no fractional part.
    """
    assert custom_round(7.0) == 7


def test_floor_infinity():
    """
    Test rounding up for infinity.
    """
    with pytest.raises(OverflowError):
        math.floor(float('inf'))


def test_floor_negative_infinity():
    """
    Test rounding up for negative infinity.
    """
    with pytest.raises(OverflowError):
        math.floor(float('-inf'))


def test_floor_nan():
    """
    Test rounding up for NaN.
    """
    with pytest.raises(ValueError):
        math.floor(float('nan'))


def test_floor_input_type_error():
    """
    Test if TypeError is raised for invalid input types.
    """
    with pytest.raises(TypeError):
        custom_round("not a number")
