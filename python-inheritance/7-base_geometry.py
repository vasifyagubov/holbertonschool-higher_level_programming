#!/usr/bin/python3
"""Write and empty class"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        """Functionnn"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if type(value) <= 0:
            raise ValueError(f"{name} must be greater than 0")
