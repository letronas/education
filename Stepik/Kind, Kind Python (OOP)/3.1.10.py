import time


class Mechanical:
    def __init__(self, date):
        self.__date = date
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        pass


class Aragon:
    def __init__(self, date):
        self.__date = date
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        pass


class Calcium:
    def __init__(self, date):
        self.__date = date
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        pass


class GeyserClassic:
    MAX_DATE_FILTER = 100
    slots = {
        1: None,  # Mechanical
        2: None,  # Aragon
        3: None  # Calcium
    }
    slots_dict = {
        1: Mechanical,  # Mechanical
        2: Aragon,  # Aragon
        3: Calcium  # Calcium
    }
    
    @classmethod
    def set_slot(cls, slot_num, filter):
        if cls.slots[slot_num] is None and cls.slots_dict[slot_num] == type(filter):
            cls.slots[slot_num] = filter
    
    def add_filter(self, slot_num, filter):
        """Добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3)
        , если он (слот) пустой (без фильтра). Также здесь следует проверять
        , что в первый слот можно установить только объекты класса Mechanical
        , во второй - объекты класса Aragon и в третий - объекты класса Calcium.
        Иначе слот должен оставаться пустым."""
        self.set_slot(slot_num, filter)
    
    @classmethod
    def remove_filter(cls, slot_num):
        """Извлечение фильтра из указанного слота (slot_num: 1, 2, и 3)"""
        cls.slots[slot_num] = None
    
    @classmethod
    def get_filters(cls):
        """Возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов)"""
        # с 3.7 такой трик прокатит
        return tuple(cls.slots.values())
    
    @classmethod
    def water_on(cls):
        """Включение воды: возвращает True, если вода течет и False - в противном случае"""
        slots_flag = all(i for i in cls.slots.values())  # если все слоты заняты
        if slots_flag:
            # все фильтры работают в пределах срока службы
            # (значение (time.time() - date) должно быть в пределах [0; MAX_DATE_FILTER])
            for i in cls.slots.values():
                if 0 <= time.time() - i.date <= cls.MAX_DATE_FILTER:
                    continue
                else:
                    slots_flag = False
                    break
        return slots_flag


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
print(my_water.slots)
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
print(my_water.slots)
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
print(my_water.slots)