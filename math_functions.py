# Ticket 6

"""
This module provides a custom implementation of the round function.
"""
import math


def custom_round(number: float) -> int:
    """
    Custom round function that wraps the built-in round function.
    Args:
    number (float): The number to round.

    Returns:
    int: The rounded integer.
    """
    if not isinstance(number, (float, int)):
        raise TypeError("Input must be a float or an integer")

    return math.floor(number)
