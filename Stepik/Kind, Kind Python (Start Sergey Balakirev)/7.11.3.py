def decorator_func(func):
    def wrapper(i_str: str):
        i_list: list = func(i_str)
        return sorted(i_list)
    return wrapper


@decorator_func
def get_list(i_str: str):
    ret_list = [int(i) for i in i_str.split()]
    return ret_list


lst = get_list(input())
print(*lst)
