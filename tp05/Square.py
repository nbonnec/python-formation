from tp05.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)
        self.__side: int = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self.length = self.width = self.__side = side

    def __str__(self):
        return f'{__class__.__name__}({self.side})'
