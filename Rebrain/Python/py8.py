# 1
import datetime

v_dict = [
    {'id': 382, 'total': 999641890816, 'used': 228013805568},
    {'id': 385, 'total': 61686008768, 'used': 52522710872},
    {'id': 398, 'total': 149023482194, 'used': 83612310700},
    {'id': 400, 'total': 498830397039, 'used': 459995976927},
    {'id': 401, 'total': 93386008768, 'used': 65371350065},
    {'id': 402, 'total': 988242468378, 'used': 892424683789},
    {'id': 430, 'total': 49705846287, 'used': 9522710872},
]


# 2 (Не закончено из-за yield
def rebrain_func_2(p_dict):
    v_icounter = 0
    for i_dict in p_dict:
        #  Вычисляет количество и процент свободной памяти на выбранном накопителе.
        v_total_space = i_dict.get('total')
        v_used_space = i_dict.get('used')
        
        v_free_space = v_total_space - v_used_space
        v_perc_usage = 100 - (v_used_space / (v_total_space / 100))
        
        if v_perc_usage < 5 or v_free_space / 1024 / 1024 / 1024 < 10:
            final_dict = {
                'id': i_dict['id'],
                'memory_status': 'memory_critical'
            }
            yield final_dict, v_icounter
        elif v_perc_usage < 10 or v_free_space / 1024 / 1024 / 1024 < 30:
            final_dict = {
                'id': i_dict['id'],
                'memory_status': 'memory_not_enough'
            }
            yield final_dict, v_icounter
        else:
            final_dict = {
                'id': i_dict['id'],
                'memory_status': 'memory_ok'
            }
            yield final_dict, v_icounter
        v_icounter += 1


# list for dicts from generator
list_of_dicts = []

for v_dct, v_cntr in rebrain_func_2(p_dict=v_dict):
    list_of_dicts.append(v_dct)
    # Решение работает, мне не нравится полный перебор каждый раз
    """
    for i in v_dict:
        if i['id'] == v_dct['id']:
            i |= v_dct
    """
    # у меня питон 3.9, по идее так норм
    v_dict[v_cntr] |= v_dct
    
print(v_dict)

super_string = '''May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated
May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...
May 20 11:01:12 PC-00102 PackageKit: daemon start
May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...
May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00
May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"
May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device
May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio
May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.
May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.'''

lst_log = super_string.split("\n")

# 6
print(sorted(lst_log, key=lambda x: datetime.datetime.strptime(x.split(" ")[2], '%H:%M:%S'))[2])
# Не понимаю, почему это тоже работает если это строка
# print(sorted(lst_log, key=lambda x: x.split(" ")[2])[2])
'''
# Проверка
# for i in lst_log:
#     print(type(i.split((" "))[2]))
#
'''

# 7
new_list = list(filter(lambda x: x.split(" ")[3] == 'PC-00102', lst_log))
print(new_list)

# 8
print(list(r[r.index(':', r.index(r.split(' ')[4])) + 1:].strip() for r in lst_log if r.split(' ')[4] == 'kernel:'))
