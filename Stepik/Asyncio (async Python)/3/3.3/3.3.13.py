import asyncio

async def compute_square(x):
    print(f"Вычисляем квадрат числа: {x}")
    await asyncio.sleep(1)  # Имитация длительной операции
    return x * x

async def main():
    # Создаём и запускаем задачи
    tasks = [asyncio.create_task(compute_square(i)) for i in range(10)]
    # Ожидаем завершения всех задач и собираем результаты

    for result in tasks:
        res = await result
        print(f"Результат: {res}")

asyncio.run(main())