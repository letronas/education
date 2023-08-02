"""
Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса.
Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None
, например:

em = EmailValidator() # None
В самом классе реализовать следующие методы класса (@classmethod):

get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxxxxx@gmail.com
, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email.
Если параметр email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False
P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""

from random import randint
from string import ascii_letters, digits


class EmailValidator:
    __email_symbols = ascii_letters + digits + '_' + '.' + '@'
    __email_symbols_length = len(__email_symbols)
    __length_min = 50
    __length_max = 100
    
    def __new__(cls, *args, **kwargs):
        return None
    
    @classmethod
    def get_random_email(cls):
        email_end = '@gmail.com'
        len_end = len(email_end)  # length of ending
        email_len = randint(1, 100 - len_end)
        left_part = ''
        for i in range(email_len):
            left_part += cls.gen_symbol(left_part, i)
        return left_part + email_end
    
    @classmethod
    def gen_symbol(cls, part, i):
        while True:
            symb = cls.__email_symbols[randint(0, cls.__email_symbols_length) - 1]
            if symb == '@':
                continue
            elif symb == (part[-1] if i != 0 else symb) == '.':  # prevent IndexError: string index out of range
                continue
            else:
                return symb
    
    @classmethod
    def check_email(cls, email: str):
        if cls.__is_email_str(email):
            email_len = len(email)  # no more 100 include
            if email_len > 100:
                return False
            
            email_in_list = email.split('@')
            cnt_at = len(email_in_list)  # should be 2, no more, no less
            if cnt_at != 2:
                return False
            if len(email_in_list[1]) > 50:
                return False
            else:
                if '..' in email_in_list[0] or '..' in email_in_list[1]:
                    return False
                
                cnt_dots_right_part = email_in_list[1].count('.')
                if cnt_dots_right_part >= 1: # changed to > from ==, because it'd be more than 1 and not ".."
                    return True
                else:
                    return False
        else:
            return False
    
    @staticmethod
    def __is_email_str(email):
        return type(email) == str


print(EmailValidator.check_email("sc_lib@list.ru"))
'''
assert EmailValidator.check_email("sc_lib@list.ru") == True , "метод check_email отработал некорректно"
assert EmailValidator.check_email("sc_lib@list_ru") == False , "метод check_email отработал некорректно"
assert EmailValidator.check_email("sc@lib@list_ru") == False , "метод check_email отработал некорректно"
assert EmailValidator.check_email("sc.lib@list_ru") == False , "метод check_email отработал некорректно"
assert EmailValidator.check_email("sclib@list.ru") == True , "метод check_email отработал некорректно"
assert EmailValidator.check_email("sc.lib@listru") == False , "метод check_email отработал некорректно"
assert EmailValidator.check_email("sc..lib@list.ru") == False, "метод check_email отработал некорректно"

m = EmailValidator.get_random_email()
assert EmailValidator.check_email(m) == True, "метод check_email забраковал сгенерированный email методом get_random_email"

assert EmailValidator() is None, "при создании объекта класса EmailValidator возвратилось значение отличное от None"

assert EmailValidator._EmailValidator__is_email_str('abc'), "метод __is_email_str() вернул False для строки"
'''