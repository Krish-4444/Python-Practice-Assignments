"""
circle.py - Module for circle calculations
"""

import math

def area(radius: float) -> float:
    """Calculate the area of a circle: π * r^2"""
    return math.pi * (radius ** 2)

def circumference(radius: float) -> float:
    """Calculate the circumference of a circle: 2 * π * r"""
    return 2 * math.pi * radius
