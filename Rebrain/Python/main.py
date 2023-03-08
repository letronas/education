v_string = '''May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated
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

# 1.Скопируйте их к себе и создайте из них список (список строк).
v_string_list = v_string.split(sep='\n')


row_num = int(input('Ведите номер строки (1-11) = '))-1 # т.к. строки начиаются с нуля

v_cstring_list = v_string_list[row_num].split()


v_full_string = v_string_list[row_num]

v_dict = dict()
v_dict = {
            'time': f"{v_cstring_list[1] +' '+ v_cstring_list[0] + '/' + v_cstring_list[2]}",
            'pc_name': v_cstring_list[3],
            'service_name': v_cstring_list[4].rstrip(':'),
            # Сообщение начинается после сервиса, поэтому нам надо найти индекс первого двоеточия после имени сервиса
            'message': v_full_string[v_full_string.index(':', v_full_string.index(v_cstring_list[4]))+1:].strip()
        }
# Всё второе задание
print(f"{v_dict.get('pc_name')} : {v_dict.get('message')} ")

#3 часть

v_list_keys = list(v_dict.keys()) #список ключей
v_new_list = ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']

new_dict = dict(zip(v_list_keys, v_new_list))
print(new_dict)

#4 task
new_lists_of_disct = list()
new_lists_of_disct.append(v_dict)
new_lists_of_disct.append(new_dict)
print(new_lists_of_disct)

#5 task
f_set = set(v_dict.values())
s_set = set(new_dict.values())

print(list(f_set & s_set))
