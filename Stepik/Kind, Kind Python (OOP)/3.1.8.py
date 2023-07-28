class Circle:
    def __init__(self, x, y, radius):  # x, y - координаты центра окружности; radius - радиус окружности
        self.x = x
        self.y = y
        self.radius = radius
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if self.check_num(x):
            self.__x = x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        if self.check_num(y):
            self.__y = y
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        if self.check_num(radius) and radius > 0:
            self.__radius = radius

    @staticmethod
    def check_num(value):
        check = type(value) in (int, float)
        if check:
            return check
        else:
            raise TypeError("Неверный тип присваиваемых данных.")
    
    def __getattr__(self, item):
        return False
        
circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует