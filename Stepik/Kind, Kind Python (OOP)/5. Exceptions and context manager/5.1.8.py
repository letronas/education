def return_value(val: str):
    try:
        if val.isdigit():
            return int(val)
        else:
            return float(val)
    except ValueError:
        return val


# считывание строки и разбиение ее по пробелам
lst_in = input().split()
lst_out = list(map(return_value, lst_in))
