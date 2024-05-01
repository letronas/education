import asyncio

async def do_work():
    await asyncio.sleep(1)
    print("Задача выполнена")

async def main():
    task = asyncio.create_task(do_work())
    await asyncio.sleep(0.5)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Задача отменена")

asyncio.run(main())