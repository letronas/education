import asyncio
places = [
   "начинает путешествие", 
   "находит загадочный лес", 
   "переправляется через реку",
   "встречает дружелюбного дракона", 
   "находит сокровище"]

roles = ["Искатель приключений", "Храбрый рыцарь", "Отважный пират"]

async def counter(name):
    for place in places:
        await asyncio.sleep(1)
        print(f"{name} {place}...")


async def main():
    task1 = asyncio.create_task(counter(roles[0]), name=f'Task-{roles[0]}')
    task2 = asyncio.create_task(counter(roles[1]), name=f'Task-{roles[1]}')
    task3 = asyncio.create_task(counter(roles[2]), name=f'Task-{roles[2]}')

    #Дождитесь выполнения всех созданных задач в главной корутине с помощью await.
    result = await asyncio.gather(task1, task2, task3)

asyncio.run(main())