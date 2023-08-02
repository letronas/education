from math import sqrt


class RadiusVector:
    def __init__(self, mandatory_arg, *args):
        self.__coords_dict = {}
        if len(args) == 0:
            for i in range(0, mandatory_arg):
                self.__coords_dict['coord_' + str(i + 1)] = 0
        else:
            self.__coords_dict['coord_1'] = mandatory_arg
            for i in range(0, len(args)):
                self.__coords_dict['coord_' + str(i + 2)] = args[i]
    
    def set_coords(self, *args):
        for i in range(min(self.__len__(), len(args))):  # иначе выйдем за пределы tuple
            self.__coords_dict['coord_' + str(i + 1)] = args[i]
    
    def get_coords(self):
        """Для получения текущих координат радиус-вектора (в виде кортежа)"""
        return tuple(self.__coords_dict.values())
    
    def __len__(self):
        """Возвращает число координат радиус-вектора (его размерность)"""
        return len(self.__coords_dict)
    
    def __abs__(self):
        """Возвращает длину радиус-вектора"""
        val = 0
        for i in self.__coords_dict.values():
            val += float(i) * float(i)
        return sqrt(val)


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)
print(res_len, res_abs)
