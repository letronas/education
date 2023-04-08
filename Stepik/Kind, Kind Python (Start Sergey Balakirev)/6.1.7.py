
some_list = input().split()

new_list = {}

for el in some_list:
    i_list = el[:2]
    if i_list in new_list:
        new_list[i_list] = new_list[i_list] + [el]
    else:
        new_list[i_list] = [el]
        
print(*sorted(new_list.items()))
