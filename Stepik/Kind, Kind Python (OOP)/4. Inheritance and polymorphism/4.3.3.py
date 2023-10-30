class Book:
    def __init__(self, title: str, author: str, pages: int, year: int):
        self.title = title  # заголовок книги (строка)
        self.author = author  # автор книги (строка)
        self.pages = pages  # число страниц (целое число)
        self.year = year  # год издания (целое число)


class DigitBook(Book):
    def __init__(self, title: str, author: str, pages: int, year: int, size, frm):
        super().__init__(title, author, pages, year)
        self.size = size  # размер книги в байтах (целое число)
        self.frm = frm  # формат книги (строка: 'pdf', 'doc', 'fb2', 'txt')

