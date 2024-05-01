import asyncio

async def coroutine_a(event_a, event_b):
    print("Корутина A: начата")
    await event_b.wait()
    print("Корутина A: ожидает корутину B")
    event_a.set()
    print("Корутина A: окончена")

async def coroutine_b(event_b, event_c):
    print("Корутина B: начата")
    await event_c.wait()
    print("Корутина B: ожидает корутину C")
    event_b.set()
    print("Корутина B: окончена")

async def coroutine_c(event_c, event_a):
    print("Корутина C: начата")
    # await event_a.wait()
    # print("Корутина C: ожидает корутину A")
    event_c.set()
    print("Корутина C: окончена")

async def main():
    # Создание событий для каждой корутины
    event_a = asyncio.Event()
    event_b = asyncio.Event()
    event_c = asyncio.Event()

    # Запуск корутин
    await asyncio.gather(
        coroutine_a(event_a, event_b),
        coroutine_b(event_b, event_c),
        coroutine_c(event_c, event_a),
    )

asyncio.run(main())