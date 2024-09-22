#!/usr/bin/python3
"""
A class used to represent a Square
"""


class Square:
    """Square class that define a square with is self size"""
    def __init__(self, size=0):
        self.size = size
    """Initialize the square with a given size"""
    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def area(self):
        return self._-size ** 2

    def my_print(self):
        """Print square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)
