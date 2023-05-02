def show_menu(func):
    def wrap(*args):
        ret_list = func(*args)
        for idx, i_value in enumerate(ret_list):
            print(f'{idx+1}. {i_value}')
    return wrap


@show_menu
def get_menu(s: str):
    new_list = s.split()
    return new_list
