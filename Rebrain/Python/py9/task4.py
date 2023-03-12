from os import getlogin
from psutil import virtual_memory

some_dict = {
    'user_name': '',
    'memory_total': '',
    'memory_used': '',
    'memory_percent': ''
}

some_dict['user_name'] = getlogin()
# достаём значение один раз
value = virtual_memory()
some_dict['memory_total'] = value[0]
some_dict['memory_used'] = value[3]
some_dict['memory_percent'] = value[2]
