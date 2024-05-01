import asyncio


async def some_coro_func(num):
    print(f"Coroutine {num} is done")


async def main():
    coro1 = some_coro_func(1)
    coro2 = some_coro_func(2)
    coro3 = some_coro_func(3)

    asyncio.gather(coro1, coro2, coro3)

asyncio.run(main())
