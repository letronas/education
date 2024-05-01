import asyncio


async def generate(num: float):
    print(f"Корутина generate с аргументом {num}")


async def main():
    var_range = range(10)
    [await generate(i) for i in var_range]


asyncio.run(main())
