import asyncio 


students = {
    "Алекс": {"course": "Асинхронный Python", "step": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "step": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "step": 491, "speed": 57}
}


async def study_course(name):
    course = students[name]["course"]
    step = students[name]["step"]
    speed = students[name]["speed"]
    print(f"{name} начал проходить курс {course}.")
    reading_time = round(step / speed, 2)
    # имитируем стороннее ожидание
    await asyncio.sleep(1)

    print(f"{name} прошел курс {course} за {reading_time} ч.")


async def main():
    task1, task2, task3 = [asyncio.create_task(study_course(name)) for name in students.keys()]
    await task1, task2, task3

asyncio.run(main())
