#!/usr/bin/python3
"""Define an empty class Rectangle."""


class Rectangle:
    """Rectangle class
    """

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self) -> int:
        """Rectange width getter
                Returns:
                        int: The width of a Rectange
                """
        return self.__width

    @width.setter
    def width(self, value):
        """Rectange width setter
                Args:
                        value (int): The value of the width
                """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self) -> int:
        """Rectange height getter
                Returns:
                        int: The height of a Rectange
                """
        return self.__height

    @height.setter
    def height(self, value):
        """Rectange height setter
                Args:
                        value (int): The value of the height
                """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
