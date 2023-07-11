'''
Подвиг 8. Объявите в программе два класса Point и Rectangle. Объекты первого класса должны создаваться командой:

pt = Point(x, y)
где x, y - координаты точки на плоскости (целые или вещественные числа). При этом в объектах класса Point должны
формироваться следующие локальные свойства:

__x, __y - координаты точки на плоскости.

и один геттер:

get_coords() - возвращение кортежа текущих координат __x, __y

Объекты второго класса Rectangle (прямоугольник) должны создаваться командами:

r1 = Rectangle(Point(x1, y1), Point(x2, y2))
или

r2 = Rectangle(x1, y1, x2, y2)
Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата (x2, y2) - правый нижний. При этом,
в объектах класса Rectangle (вне зависимости от способа их создания) должны формироваться следующие локальные свойства:

__sp - объект класса Point с координатами x1, y1 (верхний левый угол);
__ep - объект класса Point с координатами x2, y2 (нижний правый угол).

Также к классе Rectangle должны быть реализованы следующие методы:

set_coords(self, sp, ep) - изменение текущих координат, где sp, ep - объекты класса Point;
get_coords(self) - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника
(ссылки на локальные свойства __sp и __ep);
draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)". Здесь x1, y1, x2, y2 -
соответствующие числовые значения координат.

Создайте объект rect класса Rectangle с координатами (0, 0), (20, 34).

P.S. На экран ничего выводить не нужно.
'''

class Point:
    def __new__(cls, *args, **kwargs):
        if kwargs:
            if type(kwargs['x']) not in (int, float) or type(kwargs['y']) not in (int, float):
                raise ValueError('Not correct params')
        else:
            if type(args[0]) not in (int, float) or type(args[1]) not in (int, float):
                raise ValueError('Not correct params')
        
        return super().__new__(cls)
    
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.set_coords(x, y)
    
    def get_coords(self):
        return self.__x, self.__y
    
    def set_coords(self, x, y):
        self.__x = x
        self.__y = y


class Rectangle:
    def __init__(self, *args, **kwargs):
        if len(args) == 2 and type(args[0]) == Point and type(args[1]) == Point:
            self.__sp = args[0]
            self.__ep = args[1]
        elif len(args) == 4 and all([type(i) in (int, float) for i in args]):
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])
        else:
            raise ValueError('Not correct params')
    
    def set_coords(self, sp: Point, ep: Point):
        self.__sp = sp
        self.__ep = ep
    
    def get_coords(self):
        return self.__sp, self.__ep
    
    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")


rect = Rectangle(0, 0, 20, 34)
rect.draw()
pnt1 = Point(-1, 0)
pnt2 = Point(1, 1)
rect.set_coords(pnt1, pnt2)
rect.draw()