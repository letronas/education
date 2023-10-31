# считывание строки и разбиение ее по пробелам
lst_in = input().split()

sum = 0
for i in lst_in:
    try:
        sum += int(i)
    except ValueError:
        continue

print(sum)