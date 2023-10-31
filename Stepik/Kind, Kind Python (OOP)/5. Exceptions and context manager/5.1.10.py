class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
    
    def __call__(self, val):
        if type(val) != float or val < self.min_value or val > self.max_value:
            raise ValueError('значение не прошло валидацию')
        else:
            return val


class IntegerValidator(FloatValidator):
    def __call__(self, val):
        if type(val) != int or val < self.min_value or val > self.max_value:
            raise ValueError('значение не прошло валидацию')
        else:
            return val


def is_valid(lst: list, validators):
    new_list = []
    for item in lst:
        for obj in validators:
            try:
                new_list.append(obj(item))
                break
            except:
                continue
    return new_list

# fv = FloatValidator(0, 10.5)
# iv = IntegerValidator(-10, 20)
# lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
#
# print(lst_out)

print(isinstance(True, int))