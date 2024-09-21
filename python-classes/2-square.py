#!/usr/bin/python3
"""Define a class Square with private instance attribute size."""


class Square:
    """Square class with private attribute size"""
    def __init__(self, size=0) -> None:
        """Initialize Square with size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
