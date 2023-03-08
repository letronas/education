# PY04
v_list_dicts = [
    {'total': 999641890816, 'used': 228013805568},
    {'total': 61686008768, 'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768, 'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287, 'used': 9522710872},
]

#1 Запрашивает у пользователя номер накопителя, который нужно проверить.
# -1 т.к. у нас массив с 0 элемента
v_num_hdd = int(input('Какой номер накопителя нужно проверить? (1-7) '))-1;
v_usr_num_hdd = v_num_hdd+1

#2 Вычисляет количество и процент свободной памяти на выбранном накопителе.
v_total_space = v_list_dicts[v_num_hdd].get('total')
v_used_space = v_list_dicts[v_num_hdd].get('used')

v_free_space = v_total_space - v_used_space
v_perc_usage = 100 - (v_used_space / (v_total_space/100))

# если нам дали размер в байтах, то переводим в гигабайты
if v_perc_usage < 5 or v_free_space/1024/1024/1024 < 10:
    print(f'на накопителе {v_usr_num_hdd} критически мало свободного места')
elif v_perc_usage < 10 or v_free_space/1024/1024/1024 < 30:
    print(f'на накопителе {v_usr_num_hdd} мало свободного места')
else:
    print(f'на накопителе {v_usr_num_hdd} достаточно свободного места')
