class WordString:
    def __init__(self, string: str = None):
        self.__str_list = []
        self.string = string
    
    def __len__(self):
        return len(self.__str_list)
    
    def __call__(self, indx: int):
        return self.__str_list[int(indx)]
    
    @property
    def string(self):
        return self.__string
    
    @string.setter
    def string(self, string):
        self.__string = string
        self.__calc_list(self.__string)
    
    def __calc_list(self, string: str):
        self.__str_list = self.__string.split() if string else []


words = WordString()
words.string = "Курс по Python ООП xxx xx"
n = len(words)
print(n)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
