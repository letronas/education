import asyncio


# # Пример данных
# log_events = [
#     {"event": "Запрос на вход", "delay": 0.5},
#     {"event": "Запрос данных пользователя", "delay": 1.0},
#     {"event": "Обновление данных пользователя", "delay": 1.5}
# ]

async def fetch_log(event: dict):
    await asyncio.sleep(event['delay'])
    print(f"Событие: '{event['event']}' обработано с задержкой {event['delay']} сек.")


async def main():
    
    # создание жесткой ссылки
    task_list = []
    for event in log_events:
        task_list.append(asyncio.create_task(fetch_log(event)))

    # инициациируем работу и ожидание
    gather_res = await asyncio.gather(*task_list)


asyncio.run(main())