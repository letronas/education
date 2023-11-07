class DateError(Exception):
    def __str__(self):
        return "Неверный формат даты"


class DateString:
    def __new__(cls, datestr):
        if datestr:
            val_res = cls.validate_str(datestr)
            obj = super().__new__(cls)
            obj.date_string = val_res
            return obj
        else:
            print(DateError())
    
    def __str__(self):
        return self.date_string
    
    @staticmethod
    def validate_str(datestr: str):
        # считаем, точек всегда две
        day, month, year = datestr.split('.')
        
        # день
        day = int(day)
        if day < 1 or day > 31:
            raise DateError
        # месяц
        month = int(month)
        if month < 1 or month > 12:
            raise DateError
        # год
        year = int(year)
        if year < 1 or year > 3000:
            raise DateError

        
        return f'{day:02}.{month:02}.{year:04}'


def __init__(self, date_string):
    self.date_string = date_string

try:
    date_string = input()
    obj = DateString(date_string)
except:
    print(DateError())
else:
    print(obj)


# # Тесты
# date_string = '1.1.2011'
# obj = DateString(date_string)
# assert obj.date_string == '01.01.2011'
# date_string = '01.01.2011'
# obj = DateString(date_string)
# assert obj.date_string == '01.01.2011'
# date_string = '12.12.2022'
# obj = DateString(date_string)
# assert obj.date_string == '12.12.2022'
# date_string = '05.5.2022'
# obj = DateString(date_string)
# assert obj.date_string == '05.05.2022'
# date_string = '05.5.22'
# obj = DateString(date_string)
# assert obj.date_string == '05.05.0022'
# date_string = '1.2.1812'
# obj = DateString(date_string)
# assert obj.date_string == '01.02.1812'

#
# try:
#     date_string = '121.1.2011'
#     obj = DateString(date_string)
# except DateError:
#     pass
# else:
#     print(f'Здесь должна была быть ошибка (date_string = {date_string})')
#
# try:
#     date_string = '11.13.2011'
#     obj = DateString(date_string)
# except DateError:
#     pass
# else:
#     print(f'Здесь должна была быть ошибка (date_string = {date_string})')
#
# try:
#     date_string = '-1.11.2011'
#     obj = DateString(date_string)
# except DateError:
#     pass
# else:
#     print(f'Здесь должна была быть ошибка (date_string = {date_string})')
#
# try:
#     date_string = '-1.11.2011'
#     obj = DateString(date_string)
# except DateError:
#     pass
# else:
#     print(f'Здесь должна была быть ошибка (date_string = {date_string})')
#
# try:
#     date_string = '00.00.0000'
#     obj = DateString(date_string)
# except DateError:
#     pass
# else:
#     print(f'Здесь должна была быть ошибка (date_string = {date_string})')