import asyncio


async def print_message():
    while True:
        print("Имитация работы функции")
        await asyncio.sleep(1)


async def interrupt_handler(interrupt_flag):
    while True:
        # Ждем установки флага
        await interrupt_flag.wait()
        print("Произошло прерывание! В этом месте может быть установлен любой обработчик")
        # Очищаем флаг для следующего использования
        interrupt_flag.clear()


# async def main():
#     interrupt_flag = asyncio.Event()
#     t1 = asyncio.create_task(print_message())
#     t2 = asyncio.create_task(interrupt_handler(interrupt_flag))

#     while True:
#         await asyncio.sleep(3)
#         print('Flag setted')
#         # Устанавливаем флаг для прерывания
#         interrupt_flag.set()


async def main():
    # Создаем флаг interrupt_flag с помощью asyncio.Event
    interrupt_flag = asyncio.Event()
    # Создаем задачу task1 исполняющую функцию print_message
    task1 = asyncio.create_task(print_message())
    # Создаем задачу task2 исполняющую функцию interrupt_handler с interrupt_flag в качестве аргумента
    task2 = asyncio.create_task(interrupt_handler(interrupt_flag)) 
    while True:
        print('cплю')
        # Останавливаем main() на 3 секунды и запускаем задачи
        await asyncio.sleep(3)
        # Устанавливаем interrupt_flag и, как следствие завершаем task2
        interrupt_flag.set()
        # Ожидаем завершения task2, которая и так уже завершила свою работу
        # await task2
        # Создаем новую задачу task2 с interrupt_flag в качестве аргумента
        # task2 = asyncio.create_task(interrupt_handler(interrupt_flag)) 

asyncio.run(main())