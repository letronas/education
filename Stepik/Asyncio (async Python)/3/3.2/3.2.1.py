import time
import asyncio


# Объявление корутинной функции(используется "async def")
async def coro(num, seconds):
    print(f"coro{num} начала свое выполнение")
    await asyncio.sleep(seconds)
    print(f"coro{num} выполнена за {seconds} секунду(ы)")


async def main():
    # Создание объектов корутин путем вызова корутинной функции.
    coro1 = coro(1, 2)
    coro2 = coro(2, 1)
    # Ожидание последовательного выполнения задач??
    await asyncio.create_task(coro2)
    await asyncio.create_task(coro1)


async def main2():
    # Создание задач из корутины.
    coro3 = coro(3, 2)
    coro4 = coro(4, 2)
    task1 = asyncio.create_task(coro(1, 2))
    task2 = asyncio.create_task(coro(2, 1))
    # Происходит асинхронный запуск и ожидание выполнения задач.
    await task2
    await coro3
    await coro4
    await task1

# start = time.time()
# asyncio.run(main())
# print(f'Программа выполнена за {time.time()-start:.3f} секунд(ы)')

start = time.time()
asyncio.run(main2())
print(f'Программа выполнена за {time.time()-start:.3f} секунд(ы)')