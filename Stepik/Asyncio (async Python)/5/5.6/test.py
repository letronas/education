import asyncio

async def call_api(message, result):
    print(message)
    await asyncio.sleep(result)
    if result == 1:
        raise Exception(f'Корутина {result}')
    else:
        print(f'Корутина {result}: Not err')
    return result


async def main():
    # Используем asyncio.gather для одновременного вызова двух асинхронных функций и получения их результатов
    try:
        await asyncio.gather(
        call_api('Вызов API 1 ...', 1),       # Имитируем первый вызов API
        call_api('Вызов API 2 ...', 2),       # Имитируем второй вызов API
        call_api('Вызов API 3 ...', 3)        # Имитируем третий вызов API
        )
    except Exception as err:
        print('Зашли в блок исключений', err)
        for i in asyncio.all_tasks():
            print(i)
    await asyncio.sleep(1)

asyncio.run(main())