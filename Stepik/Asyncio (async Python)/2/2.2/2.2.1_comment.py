import asyncio

tasks = []

# Корутина, отвечающая за "получение" данных
async def fetch_data(n):
    # Печать сообщения о начале работы fetch_data_task_n
    print(f"Загрузка данных {(task_name := asyncio.current_task().get_name())}")
    # Имитация выполнения длительной I/O операции
    await asyncio.sleep(1)
    # Возврат "полученных" данных
    return n + 1

# Корутина, отвечающая за обработку данных
async def process_data(n):
    # Печать сообщения о начале работы process_data_task_n
    print(f"Обработка данных {(task_name := asyncio.current_task().get_name())}")
    # Имитация выполнения длительной I/O операции
    # await asyncio.sleep(1)
    # Ожидание выполнения/результатов выполнения соответствующей fetch_data_task
    data = await tasks[n][0]
    # Обработка полученных данных и возврат результата работы process_data_task_n
    return f"{task_name} вернула данные: {data * 2}"

# Базовая корутина (основной поток выполнения программы)
async def main():
    # Цикл на 500 итераций
    for i in range(10):
        # Создание кортежей пар задач для получения/обработки данных
        fetch = asyncio.create_task(fetch_data(i), name=f"fetch_data_task_{i}")
        processed = asyncio.create_task(process_data(i), name=f"process_data_task_{i}")
        # После создания каждая задача запланирована к выполнению
        # Добавление кортежей в список tasks
        tasks.append((fetch, processed))
    # Запуск на выполнение всех созданных задач на await.
    # Ожидание результата выполнения всех process_data_task - задач
    result = await asyncio.gather(*[tpl[-1] for tpl in tasks])
    # Печать списка result
    print(result)


asyncio.run(main())