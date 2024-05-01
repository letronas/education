import asyncio

news_list = [
    "Новая волна COVID-19 обрушилась на Европу",
    "Рынки акций растут на фоне новостей о вакцине",
    "Конференция разработчиков игр пройдет онлайн",
    "Открыт новый вид подводных животных"   
]


async def analyze_news(keyword, news_list, delay):
    for news in news_list:
        if keyword in news:
            print(f"Найдено соответствие для '{keyword}': {news}")
            await asyncio.sleep(1)


async def main():
    # Создаем асинхронные задачи для каждой корутины с разными ключевыми словами и задержками
    task1 = asyncio.create_task(analyze_news(keyword="COVID-19", news_list=news_list, delay=1))
    task2 = asyncio.create_task(analyze_news(keyword="игр", news_list=news_list, delay=1))
    task3 = asyncio.create_task(analyze_news(keyword="новый вид", news_list=news_list, delay=1))

    # Ожидаем выполнения всех задач
    res = await asyncio.gather(task1, task2, task3)

asyncio.run(main())