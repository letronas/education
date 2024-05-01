import asyncio
import time


async def fetch_data(simulation_delay: int, source: str) -> str:
    await asyncio.sleep(simulation_delay)
    return f"Данные из {source} получены"


async def main():
    sources1 = ["Источник 1", "Источник 2", "Источник 3"]  # Список источников данных
    sources2 = ["Источник 4", "Источник 5", "Источник 6"]  # Список источников данных
    sources3 = ["Источник 7", "Источник 8", "Источник 9"]  # Список источников данных

    # Создаем "долгую" задачу
    for num in range(3):
        source = sources1 if not num else sources2 if num == 1 else sources3
        # Использование await внутри цикла для ожидания завершения каждой итерации
        data = await asyncio.gather(fetch_data(1, source[0]), fetch_data(1, source[1]), fetch_data(1, source[2]))

        print(data)  # Вывод результата после получения данных
    # Ждем завершения работы task


start = time.time()
asyncio.run(main())
print(f'Время выполнения программы: {time.time() - start}')