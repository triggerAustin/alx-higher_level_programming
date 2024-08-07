#!/usr/bin/python3
"""
defines a class BaseGeometry
"""


class BaseGeometry:
    """
        a class BaseGeometry
    """
    def __init__(self):
        """
            constructor
        """
        pass

    def area(self):
        """
            Raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            validates value
            Args:
                name: string
                Vaulue: value to validate
        """
        if !(isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
