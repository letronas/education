import asyncio

# Список заклинаний с временем каста
# Полный список заклинаний вшит в задачу
spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 4,
    "Телепортация": 7
}

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]


# Максимальное время для каста заклинания
max_cast_time = 5  # Секунды


async def cast_spell(student, spell, cast_time):
    await asyncio.sleep(cast_time)
    if cast_time < max_cast_time:
        print(f"{student} успешно кастует {spell} за {cast_time} сек.")
    else:
        print(f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield.")

async def main():
    tasks = [asyncio.create_task(cast_spell(student, spell, cast_time))
             for student in students
             for spell, cast_time in spells.items()]
    try:
        res = await asyncio.wait_for(asyncio.shield(asyncio.gather(*tasks)), max_cast_time)
    except asyncio.TimeoutError as err:
        print("Я тута")
        await asyncio.sleep(max(value for value in spells.values()))

asyncio.run(main())
