def get_data_fig(*args, **kwargs) -> tuple:
    perim = 0
    for i in args:
        perim += int(i)
    
    list_params = ['type', 'color', 'closed', 'width']
    if set(list_params) & set(kwargs.keys()) != set():
        f_cort = (perim,)
        for i in list_params:
            if i in kwargs:
                f_cort = f_cort + (kwargs[i],)
        return f_cort
    else:
        return (perim,)


# print(get_data_fig(1, 2, color = 'red', type=True))
# print(get_data_fig(1, 2))
