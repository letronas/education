import asyncio

# Список результатов
results = []


# Корутина для создания задач
async def coro(n: int):
    await asyncio.sleep(n / 10)
    if n == 5:
        raise Exception(f'Something went wrong in coro {n}')
    results.append(f"Coroutine: {n}")
    # Если бы мы не "ломали" gather(), то эти результаты оказались бы в gather_res
    return f"Coroutine: {n}"


# Базовая корутина
async def main():
    try:
        # Ожидание результатов выполнения всех переданных в gather задач
        gather_res = await (gather_obj := asyncio.gather(*[coro(x) for x in range(10)]))

    except Exception as err:
        # Тип объекта, созданного gather()
        print(f'{type(gather_obj) = }')  # asyncio.tasks._GatheringFuture
        # Исключение всплывшее при ожидании gather()
        print(f'{gather_obj.exception() = }')
    # Даем время всем задачам выполниться.
    await asyncio.sleep(.3)

    print(f'Список результатов выполненных задач: {[result for result in results]}')


asyncio.run(main())
