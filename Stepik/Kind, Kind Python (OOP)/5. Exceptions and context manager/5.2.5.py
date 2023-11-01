class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    
    @staticmethod
    def check_val(val: str):
        try:
            if val.isdigit():
                val = int(val)
            else:
                val = float(val)
            return val
        except ValueError:
            return val


x, y = input().split(' ')
x, y = Point.check_val(x), Point.check_val(y)


if type(x) == str or type(y) == str:
    pt = Point()
else:
    pt = Point(x, y)

print(f'Point: x = {pt._x}, y = {pt._y}')
