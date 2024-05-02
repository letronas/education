import asyncio

# Полный десериализованый JSON вшит в задачу

books_json = [
    {
        "Порядковый номер": 1,
        "Автор": "Rebecca Butler",
        "Название": "Three point south wear score organization.",
        "Год издания": "1985",
        "Наличие на полке": True
    },
    {
        "Порядковый номер": 2,
        "Автор": "Mark Cole",
        "Название": "Drive experience customer somebody pressure.",
        "Год издания": "1985",
        "Наличие на полке": False
    },
    ]


async def check_book(book):
    if book["Наличие на полке"] is not True:
        return f"{book['Порядковый номер']}: {book['Автор']}: {book['Название']} ({book['Год издания']})"


async def main():
    tasks = [check_book(book) for book in books_json]
    results  = await asyncio.gather(*tasks)
    absent_books = [result for result in results if result]
    print(*absent_books, sep = '\n')


asyncio.run(main())