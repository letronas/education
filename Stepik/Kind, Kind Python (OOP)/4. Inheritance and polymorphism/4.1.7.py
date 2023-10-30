class Singleton:
    _instances = None
    
    def __new__(cls, *args, **kwargs):
        # Singleton в рамках каждого наследника
        if not isinstance(cls._instances, Singleton):
            cls._instances = super().__new__(cls)
        return cls._instances


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


# a = Game('Test')
# print(id(a))
# print(a.name)
# a = Game('Test2')
# print(id(a))
# print(a.name)
