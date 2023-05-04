def decor_param_func(start=0):  # start value for sum
    def decor_func(func):
        def wrapper(in_str: str):
            out_sum = func(in_str)
            return out_sum + start
        
        return wrapper
    
    return decor_func


@decor_param_func(start=5)
def str_to_list_sum(in_str: str) -> int:
    lst = [int(i) for i in in_str.split()]
    lsum = sum(lst)
    return lsum


s = input()
print(str_to_list_sum(s))
