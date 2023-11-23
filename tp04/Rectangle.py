from types import NotImplementedType


class Rectangle:
    """A very sophisticated class."""

    __slots__ = ('__length', '__width')

    def __init__(self, length: int, width: int):
        """
        A shiny constructor.
        :param length:
        :param width:
        """
        self.__length: int = length
        self.__width: int = width

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

    def get_surface(self) -> int:
        return self.__length * self.__width

    def __eq__(self, o: object) -> bool | NotImplementedType:
        if not isinstance(o, Rectangle):
            return NotImplemented
        return self.__length == o.__length and self.__width == o.__width

    def __str__(self) -> str:
        return f'{__class__.__name__}({self.__length=}, {self.__width=})'

    # length = property(get_length, set_length)
    # width = property(get_width, set_width)
