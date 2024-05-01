import asyncio


async def countdown(name, seconds):
    # это лучше вынести параметром, но нам не разрешили
    motivation = "Найди скрытые сокровища!" if name == "Квест на поиск сокровищ" else "Беги быстрее, дракон на хвосте!"
    for second in range(1, seconds+1)[::-1]:
        print(f"{name}: Осталось {second} сек. {motivation}")
        await asyncio.sleep(0)
    print(f"{name}: Задание выполнено! Что дальше?")


async def main():
    treasure_hunt = asyncio.create_task(countdown("Квест на поиск сокровищ", 10))
    dragon_escape = asyncio.create_task(countdown("Побег от дракона", 5))

    res = asyncio.gather(treasure_hunt, dragon_escape)


asyncio.run(main())
