import asyncio
# import time

async def print_with_delay(num: int):
    await asyncio.sleep(1)
    print(f'Coroutine {num} is done')


async def main():
    tasks = []
    for i in range(10):
        tasks.append(print_with_delay(i))

    await asyncio.gather(*tasks)

# start = time.time()
asyncio.run(main())
# print(time.time()-start)