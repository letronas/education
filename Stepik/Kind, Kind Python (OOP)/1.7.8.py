# -*- coding: cp1251 -*-

from string import ascii_uppercase, digits


class CardCheck:
    # у нас в любом случае должен быть пробел
    CHARS_FOR_NAME = ascii_uppercase + digits + ' '
    
    @staticmethod
    def check_card_number(number):
        i_list = number.split('-')
        if len(i_list) != 4:
            return False
        
        sets_digits = set(digits)
        for i in i_list:
            # Если длина формата не 4, это ошибка
            if len(i) != 4:
                return False
            # Дальше проверяем только вхождение в множество digits
            if set(i) <= sets_digits:
                continue
            else:
                return False
        # Если всё успешно, возрващаем True
        return True
    
    @classmethod
    def check_name(cls, name):
        if len(name.split(' ')) != 2:
            return False
        else:
            return set(name) <= set(cls.CHARS_FOR_NAME)


## Проверки
is_name = CardCheck.check_name("SERGEI BALAKIREV")
is_number = CardCheck.check_card_number("1244-5678-9012-0000-5643")

print(is_name)
