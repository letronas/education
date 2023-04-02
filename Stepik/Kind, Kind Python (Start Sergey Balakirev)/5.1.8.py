n = int(input())

fibb_list = []
i = 2
# предположим, ноль ввести не могут
if n == 1:
    fibb_list.append(1)
else:
    fibb_list.append(1)
    fibb_list.append(1)
    
while i < n:
    fibb_list.append(fibb_list[i-2] + fibb_list[i-1])
    i += 1
        
print(*fibb_list)