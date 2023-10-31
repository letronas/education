class Triangle:
    def __new__(cls, *args, **kwargs):
        if args:
            for i in args:
                if type(i) not in (int, float) or i <= 0:
                    raise TypeError('стороны треугольника должны быть положительными числами')
            
            if args[0] + args[1] < args[2] or args[0] + args[2] < args[1] or args[1] + args[2] < args[0]:
                raise ValueError('из указанных длин сторон нельзя составить треугольник')
        
        else:
            for i in kwargs.values():
                if type(i) not in (int, float) or i <= 0:
                    raise TypeError('стороны треугольника должны быть положительными числами')
            
            if kwargs['a'] + kwargs['b'] < kwargs['c'] or kwargs['a'] + kwargs['c'] < kwargs['b'] or kwargs['b'] + \
                    kwargs['c'] < kwargs['a']:
                raise ValueError('из указанных длин сторон нельзя составить треугольник')
        
        return super().__new__(cls)
    
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []
for i in input_data:
    try:
        lst_tr.append(Triangle(*i))
    except:
        continue
#
# print(lst_tr)
#
# for i in lst_tr:
#     print(i.__dict__)
