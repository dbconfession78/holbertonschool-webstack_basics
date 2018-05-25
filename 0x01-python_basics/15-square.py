#!/usr/bin/python3
"""
Module 15-square
"""


class Square:
    """
    class definition for 'Square'
    """
    def __init__(self, size=0):
        """
        Square class initialization
        """
        self.__size = size

    def __repr__(self):
        """
        __repr__ for the Square class
        """
        return self

    def __str__(self):
        """
        __str__ for the Square class
        """
        retval = ""
        for i in range(self.__size):
            s = ""
            if i < self.__size-1:
                s = "\n"
            retval += "{}{}".format(("#" * self.__size), s)
        return retval

    @property
    def size(self):
        """
        size: getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter
        :value: size to set
        """
        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        returns the current square area
        """
        return self.__size**2

    def my_print(self):
        """"
        prints in stdout the squre with the character #
        """
        print(str(self))
