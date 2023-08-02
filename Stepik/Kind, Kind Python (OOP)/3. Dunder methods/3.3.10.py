class PolyLine:
    def __init__(self, *args):
        self.__coord_list = list(args)
        
    def add_coord(self, x, y):
        self.__coord_list.append((x, y))
        
    def remove_coord(self, indx):
        del self.__coord_list[indx]

    def get_coords(self):
        return self.__coord_list

poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
poly.add_coord(1,1)
poly.remove_coord(1)
print(poly.get_coords())

