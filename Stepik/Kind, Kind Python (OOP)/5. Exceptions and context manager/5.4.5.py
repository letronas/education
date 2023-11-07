class PrimaryKeyError(Exception):
    def __init__(self, id=None, pk=None):
        if id is None and pk is None:
            self.msg = "Первичный ключ должен быть целым неотрицательным числом"
        elif id is not None and pk is None:
            self.msg = f"Значение первичного ключа id = {id} недопустимо"
        elif id is None and pk is not None:
            self.msg = f"Значение первичного ключа pk = {pk} недопустимо"
        else:
            # тут бы не помешала кастомка
            raise Exception
    
    def __str__(self):
        return self.msg


err = PrimaryKeyError(id=-10.5)
print(err)
