#!/usr/bin/python3
""" The above runs the program from with pyv3"""


class Square:
    """ The Class defifntion"""
    def __init__(self, size=0, position=(0, 0)):
        """ Initializing the variables
            Args: Arguements of the class
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter"""
        if (not isinstance(value, tuple) or len(value) != 2 or
           not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area"""
        return self.__size * self.__size

    def my_print(self):
        """Print the values and symbols"""
        if self.__size == 0:
            print("")
            return
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """Print the values and symbols"""
        if self.__size == 0:
            print("")
            return

        result = []
        result.extend([""] * self.__position[1])
        for _ in range(self.__size):
            line = " " * self.__position[0] + "#" * self.__size
            result.append(line)
        return "\n".join(result)
