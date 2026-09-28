"""
rectangle.py - Module for rectangle calculations
"""

def area(length: float, width: float) -> float:
    """Calculate the area of a rectangle: length * width"""
    return length * width

def perimeter(length: float, width: float) -> float:
    """Calculate the perimeter of a rectangle: 2 * (length + width)"""
    return 2 * (length + width)
