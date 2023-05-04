from functools import wraps


def decor_func(func):
    @wraps(func)
    def wrapper(*args):
        return sum(func(*args))
    return wrapper

@decor_func
def get_list(in_str: str):
    "Функция для формирования списка целых значений"
    return [int(i) for i in in_str.split()]


print(get_list.__doc__)
