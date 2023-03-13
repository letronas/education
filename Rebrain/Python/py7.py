# 1
log_msg = '''May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated
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

# 3
list_of_dicts = [
    {'id': 382, 'total': 999641890816, 'used': 228013805568},
    {'id': 385, 'total': 61686008768, 'used': 52522710872},
    {'id': 398, 'total': 149023482194, 'used': 83612310700},
    {'id': 400, 'total': 498830397039, 'used': 459995976927},
    {'id': 401, 'total': 93386008768, 'used': 65371350065},
    {'id': 402, 'total': 988242468378, 'used': 892424683789},
    {'id': 430, 'total': 49705846287, 'used': 9522710872},
]

new_list = []


# 2.1
def rows_in_list(*args, p_list):
    i = 0
    for r in args:
        i += 1
        if i in (1, 2, 4):
            v_rlist = r.split()
            # 2.2
            v_dict = {
                'time': f"{v_rlist[1] + ' ' + v_rlist[0] + '/' + v_rlist[2]}",
                'pc_name': v_rlist[3],
                'service_name': v_rlist[4].rstrip(':'),
                # Сообщение начинается после сервиса,
                # поэтому нам надо найти индекс первого двоеточия после имени сервиса
                'message': " ".join(v_rlist[4:])  # тут я переделал, так как join читается легче
            }
            # 2.3
            p_list.append(v_dict)
    return p_list


# 4.1
def dict_analyze(p_dict_list):
    final_task_dict = {}
    for i in p_dict_list:
        #  Вычисляет количество и процент свободной памяти на выбранном накопителе.
        v_total_space = i.get('total')
        v_used_space = i.get('used')
        
        v_free_space = v_total_space - v_used_space
        v_perc_usage = 100 - (v_used_space / (v_total_space / 100))
        
        if v_perc_usage < 5 or v_free_space / 1024 / 1024 / 1024 < 10:
            final_task_dict['memory_critical'] = final_task_dict.get('memory_critical', []) + list([i.get('id')])
        elif v_perc_usage < 10 or v_free_space / 1024 / 1024 / 1024 < 30:
            final_task_dict['memory_not_enough'] = final_task_dict.get('memory_not_enough', []) + list([i.get('id')])
        else:
            final_task_dict['memory_ok'] = final_task_dict.get('memory_ok', []) + list([i.get('id')])
        
        ''' Alternative solution
        if v_perc_usage < 5 or v_free_space / 1024 / 1024 / 1024 < 10:
            final_dict.update({'memory_critical' : final_dict.get('memory_critical') + list([i.get('id')])})
        elif v_perc_usage < 10 or v_free_space / 1024 / 1024 / 1024 < 30:
            final_dict.update({'memory_not_enough': final_dict.get('memory_not_enough') + list([i.get('id')])})
        else:
            final_dict.update({'memory_ok': final_dict.get('memory_ok') + list([i.get('id')])})
        '''
    return final_task_dict


def final_dict(p_state, p_final_task_dict, new_id):
    p_final_task_dict[p_state] = p_final_task_dict.get(p_state, []) + list([new_id])


print(rows_in_list(
    "Jan 09 12:56:28 PC0507 systemd[404]: Starting Docker container...",
    "May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two "
    "iterations.",
    "May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...",
    "May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...",
    "May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device",
    "May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.", p_list=new_list))

# 4.2
print(dict_analyze(p_dict_list=list_of_dicts))
