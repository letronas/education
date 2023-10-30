class Animal:
    
    def __init__(self, name: str, old: int):
        self.name = name  # название животного (строка)
        self.old = old  # возраст животного (целое число)
    
    def get_info(self):
        pass


class Cat(Animal):
    def __init__(self, name: str, old: int, color: str, weight: float):
        super().__init__(name, old)
        self.color = color
        self.weight = weight
    
    def get_info(self):
        return f'{self.name}: {self.old}, {self.color}, {self.weight}'


class Dog(Animal):
    def __init__(self, name: str, old: int, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size
    
    def get_info(self):
        return f'{self.name}: {self.old}, {self.breed}, {self.size}'


# cat = Cat('кот', 4, 'black', 2.25)
#
# print(cat.get_info())