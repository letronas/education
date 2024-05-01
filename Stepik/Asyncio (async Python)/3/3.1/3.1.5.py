import asyncio


async def async_function1():
    await asyncio.sleep(1)
    return "Func 1 completed"


async def main_func():
    result = await async_function1()
    print(result)


asyncio.run(main_func())