"""
Объявите класс AppStore - интернет-магазин приложений для устройств под iOS. В этом классе должны быть реализованы
следующие методы:

add_application(self, app) - добавление нового приложения app в магазин;
remove_application(self, app) - удаление приложения app из магазина;
block_application(self, app) - блокировка приложения app (устанавливает локальное свойство blocked объекта app в
значение True);
total_apps(self) - возвращает общее число приложений в магазине.

Класс AppStore предполагается использовать следующим образом (эти строчки в программе не писать):

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
Здесь Application - класс, описывающий добавляемое приложение с указанным именем. Каждый объект класса Application
должен содержать локальные свойства:

name - наименование приложения (строка);
blocked - булево значение (True - приложение заблокировано; False - не заблокировано, изначально False).

Как хранить список приложений в объектах класса AppStore решите сами.

P.S. В программе нужно только объявить классы с указанным функционалом.
"""

class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False


class AppStore:
    _apps_list = []
    
    @classmethod
    def add_application(cls, app):
        cls._apps_list.append(app)
    
    @classmethod
    def remove_application(cls, app):
        cls._apps_list.remove(app)
    
    @staticmethod
    def block_application(app):
        app.blocked = True
    
    @classmethod
    def total_apps(cls):
        return len(cls._apps_list)


store = AppStore()
app_youtube = Application("Youtube")
assert app_youtube.blocked == False, "начальное значение blocked должно быть равно False"

store.add_application(app_youtube)
store.block_application(app_youtube)

assert app_youtube.name == "Youtube" and app_youtube.blocked == True, "неверные значения локальных атрибутов объекта класса Application"

app_stepik = Application("Stepik")
store.add_application(app_stepik)

assert store.total_apps() == 2, "неверное число приложений в магазине"

store.remove_application(app_youtube)
assert store.total_apps() == 1, "неверное число приложений в магазине, некорректно работает метод remove_application"
