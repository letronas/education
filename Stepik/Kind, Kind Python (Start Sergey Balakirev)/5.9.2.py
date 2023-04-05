'''
some_list = [int(i) for i in input().split()]

list_len = len(some_list)

list_dimension = int(pow(list_len, 0.5))

new_list = [[some_list[j] for j in range(i, i + list_dimension)] for i in range(0, list_len, list_dimension)]

print(new_list)
'''

lst_in = list(map(int, input().split()))

N = int(len(lst_in) ** 0.5)

lst = [lst_in[i:i+N] for i in range(0, len(lst_in), N)]

print(lst)


