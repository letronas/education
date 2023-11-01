class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    @staticmethod
    def val_type_check(val):
        if type(val) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        else:
            return True
    
    @staticmethod
    def coord_position_check(val):
        if val <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        else:
            return True
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, val):
        if self.val_type_check(val):
            self._x = val
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, val):
        if self.val_type_check(val):
            self._y = val
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, val):
        if self.val_type_check(val) and self.coord_position_check(val):
            self._width = val
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, val):
        if self.val_type_check(val) and self.coord_position_check(val):
            self._height = val
    
    def is_collision(self, rect):
        if self.x + self.width < rect.x or rect.x + rect.width < self.x \
                or self.y + self.height < rect.y or rect.y + rect.height < self.y:
            pass
        else:
            raise TypeError('прямоугольники пересекаются')


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = lst_rect.copy()

for i in lst_rect:
    cnt = 0
    for j in lst_rect:
        try:
            if i != j:
                i.is_collision(j)
        except TypeError:
            cnt += 1
            if j in lst_not_collision:
                lst_not_collision.remove(j)
    if cnt != 0:
        if i in lst_not_collision:
            lst_not_collision.remove(i)


# a = Rect(0, 2, 0, 20)