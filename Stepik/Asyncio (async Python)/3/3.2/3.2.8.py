import asyncio


async def with_await():
    await asyncio.sleep(1)
    print('with_await finished')


async def without_await():
    await asyncio.sleep(1)
    print("without_await finished")


async def main():
    task_with_await = asyncio.create_task(with_await())
    task_without_await = asyncio.create_task(without_await())

    await task_with_await


asyncio.run(main())