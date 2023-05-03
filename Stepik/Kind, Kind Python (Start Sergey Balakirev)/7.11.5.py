t = {'¸': 'yo', 'à': 'a', 'á': 'b', 'â': 'v', 'ã': 'g', 'ä': 'd', 'å': 'e', 'æ': 'zh',
     'ç': 'z', 'è': 'i', 'é': 'y', 'ê': 'k', 'ë': 'l', 'ì': 'm', 'í': 'n', 'î': 'o', 'ï': 'p',
     'ð': 'r', 'ñ': 's', 'ò': 't', 'ó': 'u', 'ô': 'f', 'õ': 'h', 'ö': 'c', '÷': 'ch', 'ø': 'sh',
     'ù': 'shch', 'ú': '', 'û': 'y', 'ü': '', 'ý': 'e', 'þ': 'yu', 'ÿ': 'ya',
     ' ': '-', '"': '-', ':': '-', ';': '-', '.': '-', ',': '-', '_': '-', '-': '-'}


def decorator_func(func):
    def wrapper(in_str: str):
        out_str: str = func(in_str)
        while out_str.find('--') != -1:
            out_str = out_str.replace('--', '-')
        
        return out_str
    
    return wrapper


@decorator_func
def func_replace(in_str: str):
    in_str = in_str.lower()
    new_str = ''
    for i in in_str:
        if i in t:
            new_str += t[i]
        else:
            new_str += i
    
    return new_str

s = input()

print(func_replace(s))
