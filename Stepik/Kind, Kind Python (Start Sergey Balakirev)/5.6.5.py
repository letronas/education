import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]


flg_break = False
for i in range(5):
    for j in range(i, 5):
        if lst_in[i][j] != lst_in[j][i]:
            print('Нет')
            flg_break = True
            break
    if flg_break:
        break
else:
    print('Да')