import asyncio


async def read_book(student, time):
    print(f"{student} начал читать книгу.")
    await asyncio.sleep(time)
    print(f"{student} закончил читать книгу за {time} секунд.")


async def main():
    # Создаем задачи для асинхронного выполнения
    task_alex = asyncio.create_task(read_book('Алекс', 5))
    task_maria = asyncio.create_task(read_book('Мария', 3))
    task_ivan = asyncio.create_task(read_book('Иван', 4))

    # Объявляем ожидание выполнения
    await task_alex, task_maria, task_ivan


asyncio.run(main())
