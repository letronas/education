def decor_param_f(in_tag: str):
    def decorator_func(func):
        def wrapper(in_str: str):
            return f'<{in_tag}>{func(in_str)}</{in_tag}>'
        return wrapper
    return decorator_func


@decor_param_f(in_tag='div')
def ret_row_lower(in_str: str):
    return in_str.lower()


s = input()
print(ret_row_lower(s))
