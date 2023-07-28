class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    @property
    def a(self):
        return self.__a
    
    @a.setter
    def a(self, value):
        if self.check_number(value):
            self.__a = value
    
    @property
    def b(self):
        return self.__b
    
    @b.setter
    def b(self, value):
        if self.check_number(value):
            self.__b = value
    
    @property
    def c(self):
        return self.__c
    
    @c.setter
    def c(self, value):
        if self.check_number(value):
            self.__c = value
    
    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Denied")
        super().__setattr__(key, value)
    
    @classmethod
    def check_number(cls, value):
        if type(value) in (int, float) and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION:
            return True
        else:
            return False


d = Dimensions(10.5, 11, 12)
print(d.__dict__)
Dimensions.a = 55
d.a = 8
print(d.__dict__)
# a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# print(a, b, c)
# d.MAX_DIMENSION = 10  # exception AttributeError
