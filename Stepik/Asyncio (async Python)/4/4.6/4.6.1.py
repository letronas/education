import asyncio

bank_account = 1000


# Принимает сумму для снятия и блокировку для безопасного доступа к банковскому счету
async def withdraw_money(amount, lock):
    global bank_account

    # Используем асинхронную блокировку для безопасного доступа к банковскому счету
    async with lock:
        if bank_account >= amount:
            print(f"Снятие {amount} р. успешно")
            await asyncio.sleep(1)
            bank_account -= amount
        else:
            print("На счету недостаточно денег")


async def main():
    lock = asyncio.Lock()
    task1 = asyncio.create_task(withdraw_money(900, lock))
    task2 = asyncio.create_task(withdraw_money(900, lock))

    await asyncio.gather(task1, task2)
    print(f'Остаток средств {bank_account} р.')


asyncio.run(main())