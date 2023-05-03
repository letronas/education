def decorator_func(func):
    def wraper(*args):
        i_keys, i_values = func(*args)
        i_new_dict = dict(zip(i_keys, i_values))
        return i_new_dict
    return wraper



@decorator_func
def some_func(i_keys: str, i_values: str):
    out_keys = i_keys.split()
    out_values = i_values.split()
    return out_keys, out_values



d = some_func(input(), input())
print(*sorted(d.items()))