#!/usr/bin/python3
"""
This module defines the following class:
    Square()
"""


class Square():
    """
    This class defines some basic functions that you can do with a square
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Constructor method """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width ** 2

    def permiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 4)

    def __str__(self):
        """ Output of object as a string """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
