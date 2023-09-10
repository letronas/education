from typing import Union
class SellItem:
    def __init__(self, name: str, price: float):
        self.name = name  # название объекта продажи (строка)
        self.price = price  # цена продажи (число: целое или вещественное).
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if type(value) == str:
            self.__name = value
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if type(value) in (int, float):
            self.__price = value


class House(SellItem):
    def __init__(self, name: str, price: float, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name: str, price: float, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name: str, price: float, square):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name):
        self.name = name
        self.__obj_list = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if type(value) == str:
            self.__name = value
    
    def add_object(self, obj: Union[House, Flat, Land]):
        """Добавление нового объекта недвижимости для продажи (один из объектов классов: House, Flat, Land)"""
        self.__obj_list.append(obj)
    
    def remove_object(self, obj):
        """Удаление объекта obj из списка объектов для продажи"""
        self.__obj_list.remove(obj)
    
    def get_objects(self):
        """Возвращает список из всех объектов для продажи"""
        return self.__obj_list
    
    
ag = Agency("Рога и копыта")
ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
ag.add_object(Land("участок под застройку", 3000000, 6.74))
for obj in ag.get_objects():
    print(obj.name)

lst_houses = [x for x in ag.get_objects() if isinstance(x, House)] # выделение списка домов
print(lst_houses)