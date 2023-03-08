str_log ='''May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated
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
lst_log = str_log.split("\n")
list_dicts = []
for v_row in lst_log:
    v_list_arr = v_row.split()
    v_dict = {
        'time': f"{v_list_arr[1] + ' ' + v_list_arr[0] + '/' + v_list_arr[2]}",
        'pc_name': v_list_arr[3],
        'service_name': v_list_arr[4].rstrip(':'),
        # Сообщение начинается после сервиса, поэтому нам надо найти индекс первого двоеточия после имени сервиса
        'message': v_row[v_row.index(':', v_row.index(v_list_arr[4])) + 1:].strip()
    }
    # 2.Создайте из него список словарей, используя ключи из того же задания
    list_dicts.append(v_dict)
# 3.Выведите на экран список значений <дата/время> всех словарей. Воспользуйтесь списковым включением.
print([i['time'] for i in list_dicts])

'''
4. Измените словари в списке: создайте новый ключ 'date', перенеся в его значение дату из поля 'time'.
В поле 'time' оставьте только время.
Выведите значения для поля 'time' всех словарей в списке.
'''
for v_dict_item in list_dicts:
    v_date = v_dict_item["time"]
    v_dict_item.update({"date": v_date[:v_date.index("/")]})
print([i['date'] for i in list_dicts])
    
'''
5.Выведите список значений поля 'message' для всех логов, которые записал ПК с именем 'PC0078'.
Воспользуйтесь списковым включением.
'''
print([i['message'] for i in list_dicts if i['pc_name'] == 'PC0078'])

'''
6. Превратите список словарей логов (который вы сделали в задании 2) в словарь.
Ключами в нем будут целые числа от 100 до 110, а значениями - словари логов.
'''
v_dict_of_dicts = {}
v_key_start = 100 # лог стартует от 100
for v_dict_item in list_dicts:
    v_dict_of_dicts.update({v_key_start: v_dict_item})
    v_key_start = v_key_start + 1
    
# 7. Выведите на экран словарь лога под ключом 104.
print(v_dict_of_dicts[104])
