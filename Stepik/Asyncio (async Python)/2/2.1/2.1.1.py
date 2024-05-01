import asyncio


async def main():
    print("Hello...")
    await asyncio.sleep(222)
    print('World!')

asyncio.run(main())