import pytest
from math_functions import custom_round

def test_round_up():
    assert custom_round(2.5) == 3

def test_round_down():
    assert custom_round(2.4) == 2

# Add more tests for edge cases, negative numbers, etc.
