import asyncio

async def countdown(n):
    counter = n
    while counter>= 0:
        print(f"{counter = }")
        await asyncio.sleep(.1)
        counter -= 1
    print(f"Отсчет завершен")

async def coro():
    print(f"Запуск корутины")
    await asyncio.sleep(.5)
    print(f"Корутина Завершена")

async def main():
        task = asyncio.create_task(countdown(10))
        # Запуск задачи до запуска корутины
        # await asyncio.sleep(0)
        await coro()
        await task

asyncio.run(main())