import asyncio                          

def print_log() -> None:
    print(f'{"":#>50}',
          f'{asyncio.get_running_loop()._ready = }',
          f'{"":->50}',
          f'{asyncio.get_running_loop()._scheduled = }',
          f'{"":->50}',
          *asyncio.all_tasks(),
          f'{"":#>50}',
          '',
          sep='\n')
async def call_api(message, result, delay=3):  
    print(message)                            
    # await asyncio.sleep(5) 
    if result == 1 or result == 2:
        raise Exception(f'Корутина {result}')
    else:
        print('Not err')
    await asyncio.sleep(delay) 
    print('A lot of waiting')
    return result                             


async def main():        
    # Используем asyncio.gather для одновременного вызова двух асинхронных функций и получения их результатов                    
    try:
        async with asyncio.TaskGroup() as tg:             
            t1 = tg.create_task(call_api('Вызов API 1 ...', 1))       # Имитируем первый вызов API
            t2 = tg.create_task(call_api('Вызов API 2 ...', 2))       # Имитируем второй вызов API
            t3 = asyncio.shield(tg.create_task(call_api('Вызов API 3 ...', 3)))        # Имитируем третий вызов API
            
    except Exception as err:
        print('Зашли в главный блок исключений', err)                         

    print(t1, t2, t3, sep='\n')


asyncio.run(main())  