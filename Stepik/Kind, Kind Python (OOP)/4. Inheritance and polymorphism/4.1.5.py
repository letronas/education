class Thing:
    id = 0
    
    @classmethod
    def id_incr(cls):
        cls.id = cls.id + 1
        return cls.id
    
    def __init__(self, name: str, price: float):
        self.id = Thing.id_incr()
        self.name = name  # наименование товара (строка)
        self.price = price  # цена товара (вещественное число)
        self.weight = None  # вес товара (вещественное число)
        self.dims = None  # длина, ширина, глубина - габариты товара (вещественные числа)
        self.memory = None  # занимаемый размер (в байтах - целое число)
        self.frm = None  # формат данных (строка: pdf, docx и т.п.)
    
    def get_data(self):
        return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)


class Table(Thing):
    def __init__(self, name: str, price: float, weight: float, dims):  #: tuple[float, ...]):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name: str, price: float, memory: int, frm: str):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm

# table = Table("Круглый", 1024, 812.55, (700, 750, 700))
# book = ElBook("Python ООП", 2000, 2048, 'pdf')
# print(*table.get_data())
# print(*book.get_data())
