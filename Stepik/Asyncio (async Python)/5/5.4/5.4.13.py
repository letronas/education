import asyncio

status_list = [
    "Отлично", "Хорошо", "Удовлетворительно", "Средне",
    "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
    "Критично", "Катастрофически"
]


async def monitor_cpu(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        if status == "Катастрофически":
            print(f"[{task_name}] Статус проверки: {status}")
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            return "Finish"
        else:
            print(f"[{task_name}] Статус проверки: {status}")
            await asyncio.sleep(0)
    return "Finish"


async def monitor_memory(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        if status == "Катастрофически":
            print(f"[{task_name}] Статус проверки: {status}")
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            return "Finish"
        else:
            print(f"[{task_name}] Статус проверки: {status}")
            await asyncio.sleep(0)
    return "Finish"


async def monitor_disk_space(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        if status == "Катастрофически":
            print(f"[{task_name}] Статус проверки: {status}")
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            return "Finish"
        else:
            print(f"[{task_name}] Статус проверки: {status}")
            await asyncio.sleep(0)
    return "Finish"


async def main():
    cpu_task = asyncio.create_task(monitor_cpu(status_list=status_list), name="CPU")
    ram_task = asyncio.create_task(monitor_memory(status_list=status_list), name="Память")
    drive_task = asyncio.create_task(monitor_disk_space(status_list=status_list), name="Дисковое пространство")

    res = await asyncio.gather(cpu_task, ram_task, drive_task)

asyncio.run(main())
