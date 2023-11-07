def input_int_numbers():
    try:
        while True:
            tmp_lst = []
            str_lst = input().split(' ')
            try:
                for i in str_lst:
                    tmp_lst.append(int(i))
            except:
                raise TypeError('все числа должны быть целыми')
            else:
                print(*tmp_lst)
                break
    
    except TypeError:
        input_int_numbers()


input_int_numbers()
