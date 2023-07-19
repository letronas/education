class Course:
    def __init__(self, name: str):
        self.name = name
        self.modules: list = []
    
    def add_module(self, module):
        self.modules.append(module)
    
    def remove_module(self, indx: int):
        del self.modules[indx]


class Module:
    def __init__(self, name: str):
        self.name = name  # название модуля;
        self.lessons: list = []
    
    def add_lesson(self, lesson):
        self.lessons.append(lesson)
    
    def remove_lesson(self, indx: int):
        del self.lessons[indx]


class LessonItem:
    def __init__(self, title: str, practices: int, duration: int):
        self.title = title  # название урока (строка)
        self.practices = practices  # число практических занятий (целое положительное число);
        self.duration = duration  # общая длительность урока (целое положительное число).
    
    def __setattr__(self, key, value):
        if (key == 'title' and type(value) != str) or (
                key in ('practices', 'duration') and type(value) != int and value <= 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            self.__dict__[key] = value
    
    def __getattr__(self, item):
        """Логика работы с несуществующими данными"""
        return False
    
    def __delattr__(self, item):
        if item not in ('title', 'practices', 'duration'):
            del self.__dict__[item]


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)

print(course.name, course.modules[0].name, course.modules[0].lessons[0].title, course.modules[0].lessons[1].title,
      course.modules[0].lessons[2].title, sep='\n')
