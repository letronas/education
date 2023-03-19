from os import getlogin as get_pc_logic
from  psutil import virtual_memory as get_pc_memory


class PCMemory:
    # 1.1.
    def __init__(self, pc_id, user_name, memory_total, memory_used, memory_percent=None):
        self.pc_id = pc_id
        self.user_name = user_name
        self.memory_total = memory_total
        self.memory_used = memory_used
        if memory_percent:
            self.memory_percent = memory_percent
        else:
            self.memory_percent = round((memory_used / memory_total) * 100, 1)
    
    # 1.2
    def show_used_percent(self):
        print(f'PC with id {self.pc_id} used {self.memory_percent} percent of memory')
    
    # 1.3
    def is_enough_memory(self):
        if self.memory_percent < 10:
            return False
        else:
            return True


pc_mem = get_pc_memory()
# Параметры указал для себя явно, просто так. Привычки из PL/SQL, кажется это правильным
new_pc = PCMemory(pc_id=1, user_name=get_pc_logic(), memory_total=pc_mem[0], memory_used=pc_mem[0]-pc_mem[1])

new_pc.show_used_percent()
print(new_pc.is_enough_memory())
