import asyncio
import time


async def fetch_data():
    print("Получение данных #1 ...")
    await asyncio.sleep(2)
    print("Данные #1 получены.")
    data = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 3}
    return data


def process_data(data: dict):
    result = sum(x for x in data.values())
    print(f"Данные обработаны: {result}")


async def main():
    task = asyncio.create_task(fetch_data())
    print("Запрос данных...")
    data = await task

    process_data(data)


asyncio.run(main())