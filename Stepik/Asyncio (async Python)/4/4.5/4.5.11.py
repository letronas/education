import asyncio
import time

global_counter = 0
lock = asyncio.Lock()

async def increment():
    global global_counter
    async with lock:
        temp = global_counter
        await asyncio.sleep(.01) # оставил номинально, но смысла не имеет
        global_counter = temp + 2.39

async def main():
    start = time.time()
    while True:
        await asyncio.gather(*[increment() for x in range(99)])
        await asyncio.sleep(60)
        print(time.time() - start)
        

asyncio.run(main())
