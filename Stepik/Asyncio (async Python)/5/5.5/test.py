# Максимальное время для каста заклинания
import asyncio

max_cast_time = 5  # Секунды
spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 4,
    "Вихрь ветра": 5,
    "Лечебное зелье": 1,
    "Призыв зверя": 6,
    "Невидимость": 4,
    "Защитный барьер": 3,
    "Телепортация": 7,
    "Призыв дождя": 2,
}
# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]

async def cast_spell(student, spell, cast_time):

    # Имитация каста заклинания
    await asyncio.sleep(cast_time)

    return f"{student} успешно кастует {spell} за {cast_time} сек."


async def cast_all_spells_for_student(student):
    for spell, cast_time in spells.items():
        task = asyncio.create_task(cast_spell(student, spell, cast_time))

        try:
            # Используем shield для защиты задачи от отмены
            await asyncio.wait_for(asyncio.shield(task), timeout=max_cast_time)
        except asyncio.TimeoutError:
            print(f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield.")
            result = await task  # Дожидаемся результата после истечения таймаута
            print(result)
        else:
            result = await task  # Получаем результат успешного каста
            print(result)


async def main():
    tasks = [cast_all_spells_for_student(student) for student in students]
    await asyncio.gather(*tasks)


asyncio.run(main())