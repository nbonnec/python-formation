import math

from tp05.ICalcGeo import ICalcGeo


class Circle(ICalcGeo):
    def __init__(self, radius: int):
        self.__radius: int = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @property
    def surface(self):
        return math.pi * self.__radius ** 2

    def __str__(self):
        return f'{__class__.__name__}({self.__radius})'
