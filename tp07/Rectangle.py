from typing import Self
from types import NotImplementedType
from tp05.ICalcGeo import ICalcGeo


class Rectangle(ICalcGeo):
    """A very sophisticated class."""

    __slots__ = ('__length', '__width')
    __instance_count: int = 0

    def __init__(self, length: int, width: int):
        """
        A shiny constructor.
        :param length:
        :param width:
        """
        self.__length: int = length
        self.__width: int = width
        Rectangle.__instance_count += 1

    @classmethod
    def build_from_str(cls, string: str):
        length, width = string.split(sep='x')
        return cls(int(length), int(width))

    @staticmethod
    def get_instance_count() -> int:
        return Rectangle.__instance_count

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def surface(self) -> float:
        return self.__length * self.__width

    def __eq__(self, o: object) -> bool | NotImplementedType:
        if not isinstance(o, Rectangle):
            return NotImplemented
        return self.__length == o.__length and self.__width == o.__width

    def __str__(self) -> str:
        return f'{__class__.__name__}({self.__length=}, {self.__width=})'

    # length = property(get_length, set_length)
    # width = property(get_width, set_width)
