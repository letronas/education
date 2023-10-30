class Vector:
    def __init__(self, *args, ):
        self.__dict_cords = {}
        for i in range(0, len(args)):
            self.__dict_cords['x' + str(i + 1)] = args[i]
    
    def get_coords(self):
        return tuple(self.__dict_cords.values())
    
    def __add__(self, other):
        s1 = self.get_coords()
        s2 = other.get_coords()
        s1_len = len(s1)
        s2_len = len(s2)
        
        new_set = list()
        for i in range(s1_len):
            new_set.append(s1[i] + s2[i])
        
        if self.__class__ == VectorInt or other.__class__ == VectorInt:
            return self.return_class_logic(new_set)
        else:
            return Vector(*new_set)
    
    def __sub__(self, other):
        s1 = self.get_coords()
        s2 = other.get_coords()
        s1_len = len(s1)
        s2_len = len(s2)
        
        new_set = list()
        for i in range(s1_len):
            new_set.append(s1[i] - s2[i])
        
        if self.__class__ == VectorInt or other.__class__ == VectorInt:
            return self.return_class_logic(new_set)
        else:
            return Vector(*new_set)
    
    @staticmethod
    def return_class_logic(new_set: set):
        for i in new_set:
            if type(i) != int:
                return Vector(*new_set)
        return VectorInt(*new_set)


class VectorInt(Vector):
    def __init__(self, *args):
        for i in args:
            if type(i) != int:
                raise ValueError('координаты должны быть целыми числами')
        
        super().__init__(*args)


# v1 = VectorInt(1, 2, 3, 4)
# v2 = Vector(1, 2, 3, 4)  # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
# print(v1.get_coords())
# print(v2.get_coords())
# v = v1 + v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
# print(v)
# v = v1 - v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
# print(v)

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
assert (v1 + v2).get_coords() == (
    4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
    -2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
