'''
import copy

var_i = int(input())
new_array = [0 for i in range(var_i)]
final_array = []


for i in range(0, var_i):
    new_array_i = copy.copy(new_array)
    new_array_i[i] = 1
    final_array.append(copy.deepcopy(new_array_i))


[print(*i) for i in final_array]

'''

var_i = int(input())

final_array = [[1 if i == j else 0 for i in range(var_i)] for j in range(var_i)]

[print(*i) for i in final_array]
