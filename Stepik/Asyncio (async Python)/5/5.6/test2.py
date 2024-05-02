import asyncio

async def factorial(name, number, raise_exception=False):
    # If raise_exception is True, will raise an exception when
    # the loop counter > 3
    f = 1
    for i in range(2, number + 1):
        print(f'  Task {name}: Compute factorial({i})...')

        if raise_exception and i > 3:
            print(f'  Task {name}: raising Exception')
            raise Exception(f'Bad Task {name}')

        await asyncio.sleep(1)
        f *= i
    print(f'==>> Task {name} DONE: factorial({number}) = {f}')
    return f

async def main():
    tasks = [factorial('A', 5),  # this will not be finished
             factorial('B', 10, raise_exception=True),
             factorial('C', 2)]

    try:
        results = await asyncio.gather(*tasks)
        print('Results:', results)
    except Exception as e:
        print('Got an exception:', e)


asyncio.run(main())