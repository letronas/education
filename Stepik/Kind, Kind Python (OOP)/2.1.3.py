"""
Подвиг 3. Объявите класс с именем Clock и определите в нем следующие переменные и методы:

- приватная локальная переменная time для хранения текущего времени, целое число (своя для каждого объекта класса Clock
с начальным значением 0);
- публичный метод set_time(tm) для установки текущего времени (присваивает значение tm приватному локальному свойству
time, если метод check_time(tm) возвратил True);
- публичный метод get_time() для получения текущего времени из приватной локальной переменной time;
- приватный метод класса check_time(tm) для проверки корректности времени в переменной tm (возвращает True, если
значение корректно и False - в противном случае).

Проверка корректности выполняется по критерию: tm должна быть целым числом, больше или равна нулю и меньше 100 000.

Объекты класса Clock предполагается использовать командой:

clock = Clock(время)
Создайте объект clock класса Clock и установите время, равным 4530.

P.S. На экран ничего выводить не нужно.
"""
class Clock:
    def __new__(cls, *args, **kwargs):
        if kwargs:
            ch_t = cls.__check_time(kwargs['tm'])
        else:
            ch_t = cls.__check_time(args[0])
        
        return super().__new__(cls) if ch_t else ''
    
    def __init__(self, tm):
        self.__time = tm
    
    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm
    
    def get_time(self):
        return self.__time
    
    @classmethod
    def __check_time(cls, tm):
        return isinstance(tm, int) and 0 <= tm < 100000


clock = Clock(4530)
'''
assert isinstance(clock, Clock) and hasattr(Clock, 'set_time') and hasattr(Clock, 'get_time'), "в классе Clock присутствуют не все методы"

assert clock.get_time() == 4530, "текущее время в объекте clock не равно 4530"

clock.set_time(10)
assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"
clock.set_time(-10)
assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"
clock.set_time(1000001)
assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"

'''