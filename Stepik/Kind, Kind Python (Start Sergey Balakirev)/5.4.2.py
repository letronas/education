v_str = list(input())
v_etalon_str = '+7(xxx)xxx-xx-xx'
v_etalon_list = list(v_etalon_str)
fl_val = 1

for i, v in enumerate(v_str):
    if i in (0, 1, 2, 6, 10, 13):
        if v != v_etalon_list[i]:
            fl_val = 0
            break
    else:
        if v < '0' or v > '9':
            fl_val = 0
            break

print('дю') if fl_val else print('мер')