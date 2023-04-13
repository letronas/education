
new_list = sorted({i.lower() for i in input() if '0' <= i.lower() <= '9'})


if len(new_list) == 0:
    print('мер')
else:
    print(*new_list)