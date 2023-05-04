t = {'¸': 'yo', 'à': 'a', 'á': 'b', 'â': 'v', 'ã': 'g', 'ä': 'd', 'å': 'e', 'æ': 'zh',
     'ç': 'z', 'è': 'i', 'é': 'y', 'ê': 'k', 'ë': 'l', 'ì': 'm', 'í': 'n', 'î': 'o', 'ï': 'p',
     'ð': 'r', 'ñ': 's', 'ò': 't', 'ó': 'u', 'ô': 'f', 'õ': 'h', 'ö': 'c', '÷': 'ch', 'ø': 'sh',
     'ù': 'shch', 'ú': '', 'û': 'y', 'ü': '', 'ý': 'e', 'þ': 'yu', 'ÿ': 'ya',
     ' ': '-'}


def decor_param_func(chars='!?'):
    def decorator_func(func):
        def wrapper(in_str: str):
            new_str_in: str = func(in_str, dict(zip(list(chars), '-' * len(chars))))
            final_str: str = func(new_str_in)
            while '--' in final_str:
                final_str = final_str.replace('--', '-')
            return final_str
        
        return wrapper
    
    return decorator_func


@decor_param_func(chars="?!:;,. ")
def replace_lat_str(in_str: str, char_dict_or_list=t):
    new_str = ''
    for i in in_str:
        if i in char_dict_or_list:
            new_str += char_dict_or_list[i]
        else:
            new_str += i
    return new_str


s = input().lower()
print(replace_lat_str(s))
