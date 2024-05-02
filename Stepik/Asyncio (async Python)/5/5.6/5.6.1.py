import asyncio                          

async def call_api(message, result, delay=3):  
    print(message)                            
    await asyncio.sleep(delay) 
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
        await asyncio.gather(              
        call_api('Вызов API 1 ...', 1),       # Имитируем первый вызов API
        call_api('Вызов API 2 ...', 2),       # Имитируем второй вызов API
        call_api('Вызов API 3 ...', 3),        # Имитируем третий вызов API
        )
    except Exception as err:
        print('Зашли в блок исключений', err)                           

asyncio.run(main())  