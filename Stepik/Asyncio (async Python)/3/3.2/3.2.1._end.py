import asyncio, random


async def cook_dish(n, tm):
    print(f"Повар {n} начинает готовить")       
    await asyncio.sleep(tm)                      
    print(f"Повар {n} закончил готовить")       
    return f"Блюдо от повара {n}"              


# Создание задач из корутин, которые представляют собой приготовление блюда каждым поваром.
async def main():
    tasks = [asyncio.create_task(cook_dish(n, random.randint(0,3))) for n in range(1, 4)]  
    print(await asyncio.gather(*tasks))  
    print('Конец main')                             


asyncio.run(main())