class RadiusVector:
    def __init__(self, *args):
        self.coords = [0] * args[0] if len(args) == 1 else [*args]

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return sum([i * i for i in self.coords]) ** 0.5

    def set_coords(self, *coord):
        self.coords = list(coord[:len(self.coords)]) + self.coords[len(coord):]

    def get_coords(self):
        return tuple(self.coords)
    
    
vector3D = RadiusVector(3)
print(vector3D.coords)
vector3D.set_coords(3, -5.6, 8)
print(vector3D.coords)
# a, b, c = vector3D.get_coords()
# vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
# vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
# res_len = len(vector3D)  # res_len = 3
# res_abs = abs(vector3D)
# print(res_len, res_abs)