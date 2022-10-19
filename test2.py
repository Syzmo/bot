class Add:
    def __init__(self, inter: int):
        if not isinstance(inter, int):
            raise TypeError("Цифры должен быть целым числом")
        self.inter = inter
    def __add__(self, other):
        return self.inter + other
class mul:
    def __init__(self, inter: int):
        if not isinstance(inter, int):
            raise TypeError("Цифры должен быть целым числом")
        self.inter = inter
    def __mul__(self, other):
        return self.inter * other
class sub:
    def __init__(self, inter: int):
        if not isinstance(inter, int):
            raise TypeError("Цифры должен быть целым числом")
        self.inter = inter
    def __sub__(self, other):
        return self.inter - other
class Truediv:
    def __init__(self, inter: int):
        if not isinstance(inter, int):
            raise TypeError("Цифры должен быть целым числом")
        self.inter = inter
    def __truediv__(self, other):
        return self.inter / other


