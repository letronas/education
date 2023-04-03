import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]


some_flag = 0
for i in range(1, 5):
    for j in range(1, 5):
        if lst_in[i-1][j-1] + lst_in[i-1][j] + lst_in[i][j-1] + lst_in[i][j] >= 2:
            print('НЕТ')
            some_flag = 1
            break
    if some_flag == 1:
        break
else:
    print('ДА')