import asyncio

balance = 100

async def withdraw(amount):
    global balance
    if balance >= amount:
        await asyncio.sleep(0.1)  # Имитация проверки баланса
        balance -= amount
        return True
    return False

async def main():
    transaction1 = asyncio.create_task(withdraw(100))
    transaction2 = asyncio.create_task(withdraw(100))
    results = await asyncio.gather(transaction1, transaction2)
    print(type(results))
    print("Transactions successful:", results)

asyncio.run(main())
print("Final balance:", balance)