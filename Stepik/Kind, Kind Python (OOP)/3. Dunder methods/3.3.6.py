import math


class Complex:
    def __init__(self, real, img):
        self.real = real  # действительная часть комплексного числа (целое или вещественное значение)
        self.img = img  # мнимая часть комплексного числа (целое или вещественное значение)
    
    @property
    def real(self):
        return self.__real
    
    @real.setter
    def real(self, value):
        self.__real = self.check_number(value)
    
    @property
    def img(self):
        return self.__img
    
    @img.setter
    def img(self, value):
        self.__img = self.check_number(value)
    
    @staticmethod
    def check_number(value):
        if type(value) not in (float, int):
            raise ValueError("Неверный тип данных.")
        else:
            return value
    
    def __abs__(self):
        return math.sqrt(self.__real * self.__real + self.__img * self.__img)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
#print(c_abs)