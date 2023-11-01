a, b = input().split(' ')
try:
    a, b = int(a), int(b)
except ValueError:
    try:
        a, b = float(a), float(b)
    except ValueError:
        pass
finally:
    print(a + b)

