import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

lst_out = [i for i_list in lst_in[::-1] for i in i_list[::-1]]


print(*lst_out)