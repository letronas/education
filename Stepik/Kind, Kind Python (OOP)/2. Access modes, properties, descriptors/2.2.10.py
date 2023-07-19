"""
Вы создаете телефонную записную книжку. Она определяется классом PhoneBook. Объекты этого класса создаются командой:

p = PhoneBook()
А сам класс должен иметь следующий набор методов:

add_phone(phone) - добавление нового номера телефона (в список);
remove_phone(indx) - удаление номера телефона по индексу списка;
get_phone_list() - получение списка из объектов всех телефонных номеров.

Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:

note = PhoneNumber(number, fio)
где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра);
fio - Ф.И.О. владельца номера (строка).

В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:

number - номер телефона (число);
fio - ФИО владельца номера телефона.

Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.
"""


class PhoneNumber:
    def __new__(cls, *args, **kwargs):
        if kwargs:
            if cls.check_num(kwargs['number']) and cls.check_fio(kwargs['fio']):
                return super().__new__(cls)
        else:
            if cls.check_num(args[0]) and cls.check_fio(args[1]):
                return super().__new__(cls)
            else:
                print("Некорректное создание объекта")
    
    def __init__(self, number: int, fio: str):
        self.number = number
        self.fio = fio
    
    @staticmethod
    def check_num(value):
        if type(value) != int or len(str(value)) != 11:
            return False
        else:
            return True
    
    @staticmethod
    def check_fio(value: str):
        if type(value) != str:  # or len(value.split(' ')) != 3: # оказалось, мы к такому не готовы
            return False
        else:
            return True


class PhoneBook:
    phone_list: list = []
    
    @classmethod
    def add_phone(cls, phone: PhoneNumber):
        cls.phone_list.append(phone)
    
    @classmethod
    def remove_phone(cls, indx):
        cls.phone_list.pop(indx)
    
    @classmethod
    def get_phone_list(cls):
        return cls.phone_list


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()

for i in phones:
    print(i.number, i.fio)
