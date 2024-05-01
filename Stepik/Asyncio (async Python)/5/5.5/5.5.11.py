import asyncio

# # Словарь бегунов: Имя + скорость бега (м/с)
# # Полный список бегунов скрыт под капотом задачи.
# runners = {
#     "Молния Марк": 12.8,
#     "Молния Марк2": 0.001,
#     "Ветреный Виктор": 13.5,
#     "Скоростной Степан": 11.2,
#     "Быстрая Белла": 10.8,
#     "Быстрая Белла2": 0.1,

# }


async def run_lap(name: str, speed: float, distance: int = 100):
    time_needed = round(distance / speed, 2)
    await asyncio.sleep(time_needed)
    print(f"{name} завершил круг за {time_needed} секунд")


async def main(max_time=10):  # Максимальное время для завершения круга 10 сек
    tasks = [asyncio.create_task(run_lap(name, speed)) for name, speed in runners.items()]
    try:
        await asyncio.wait_for(asyncio.gather(*tasks), max_time)
    except asyncio.TimeoutError:
        pass

asyncio.run(main())