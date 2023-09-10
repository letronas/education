class Thing:
    def __init__(self, name: str, weight: float):
        self.name = name  # наименование предмета (строка)
        self.weight = weight  # вес предмета (вещественное число)
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if type(value) == str:
            self.__name = value
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        if type(value) == float:
            self.__weight = value


class ArtObject(Thing):
    """Для представления арт-объектов"""
    
    def __init__(self, name: str, weight: float, author: str, date: str):
        super().__init__(name, weight)
        self.author = author  # author - автор (строка)
        self.date = date  # date - дата создания (строка)
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, value):
        if type(value) == str:
            self.__author = value
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, value):
        if type(value) == str:
            self.__date = value


class Computer(Thing):
    """Для системных блоков компьютеров"""
    
    def __init__(self, name: str, weight: float, memory: int, cpu: str):
        super().__init__(name, weight)
        self.memory = memory  # memory - размер памяти (целое число);
        self.cpu = cpu  # cpu - тип процессора (строка)
    
    @property
    def memory(self):
        return self.__memory
    
    @memory.setter
    def memory(self, value):
        if type(value) == int:
            self.__memory = value
    
    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, value):
        if type(value) == str:
            self.__cpu = value


class Auto(Thing):
    """Для автомобилей"""
    
    def __init__(self, name: str, weight: float, dims: tuple, model: str = ''):
        super().__init__(name, weight)
        self.dims = dims  # dims - габариты, кортеж (width, length, height) - вещественные или целые числа
        self.model = model
    
    @property
    def dims(self):
        return self.__dims
    
    @dims.setter
    def dims(self, value):
        if type(value) == tuple and all(type(i) in (int, float) for i in value):
            self.__dims = value
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if type(value) == str:
            self.__model = value


class Mercedes(Auto):
    def __init__(self, name: str, weight: float, dims: tuple, model: str, old: int):
        super().__init__(name, weight, dims, model)  # странно, что модель не в базовом классе, переместил туда
        self.old = old
    
    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, value):
        if type(value) == int:
            self.__old = value


class Toyota(Auto):
    def __init__(self, name: str, weight: float, dims: tuple, model: str, wheel: bool):
        super().__init__(name, weight, dims, model)  # странно, что модель не в базовом классе, переместил туда
        self.wheel = wheel
    
    @property
    def wheel(self):
        return self.__wheel
    
    @wheel.setter
    def wheel(self, value):
        if type(value) == bool:
            self.__wheel = value


c = Auto('Test', 1.0, (1, 3.0, 4))
print(c.__dict__)
