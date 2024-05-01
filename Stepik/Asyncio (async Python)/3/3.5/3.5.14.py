import asyncio

# Counter 1 - имя счётчика
# 13 - максимальное значение для счётчика Counter_1 

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0,
    "Counter 3": 0
}


delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}


async def counter(counter_name, delay):
    for i in range(max_counts[counter_name]):
        counters[counter_name] += 1
        print(f"{counter_name}: {counters[counter_name]}")
        await asyncio.sleep(delay)


async def main():
        task1 = asyncio.create_task(counter('Counter 1', delays["Counter 1"]))
        task2 = asyncio.create_task(counter('Counter 2', delays["Counter 2"]))
        task3 = asyncio.create_task(counter('Counter 3', delays["Counter 3"]))
        await task1
        await task2
        await task3

asyncio.run(main())
