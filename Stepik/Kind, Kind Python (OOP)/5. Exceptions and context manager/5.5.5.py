class Box:
    def __init__(self, name: str, max_weight):  # int | float):
        self._name = name  # название ящика
        self._max_weight = max_weight  # максимальный суммарный вес вещей в ящике (любое положительное число)
        self._things = []
        self.__current_weight = 0
    
    def add_thing(self, obj):
        weight = obj[1]
        if self.__current_weight + weight < self._max_weight:
            self._things.append(obj)
            self.__current_weight += weight
        else:
            raise ValueError('превышен суммарный вес вещей')


class BoxDefender:
    def __init__(self, link):
        self.obj = link
    
    def __enter__(self):
        self.obj._things_copy = self.obj._things[:]
        return self.obj
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.obj._things = self.obj._things_copy

#
# b = Box('name', 2000)
# assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"
#
# b.add_thing(("1", 100))
# b.add_thing(("2", 200))
#
# try:
#     with BoxDefender(b) as bb:
#         bb.add_thing(("3", 1000))
#         bb.add_thing(("4", 1900))
# except ValueError:
#     assert len(b._things) == 2
#
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# try:
#     with BoxDefender(b) as bb:
#         bb.add_thing(("3", 100))
# except ValueError:
#     assert False, "возникло исключение ValueError, хотя, его не должно было быть"
# else:
#     assert len(b._things) == 3, "неверное число элементов в списке _things"
