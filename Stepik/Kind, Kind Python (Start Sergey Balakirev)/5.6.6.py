some_list = list(map(int, input().split()))

list_len = len(some_list)

for i in range(list_len):
    for j in range(i+1, list_len):
        if some_list[j] < some_list[i]:
            some_list[i], some_list[j] = some_list[j], some_list[i]
            
print(*some_list)
