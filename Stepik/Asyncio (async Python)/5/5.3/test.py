# SuperFastPython.com
# example of starting a new task without asyncio.sleep(0)
import asyncio
 
# a background task
async def other_task():
    # report a message
    print('Other task is running')
    # prepare some data and return it
    await asyncio.sleep(9999)
    return 99
 
# entry point coroutine
async def main():
    # create and schedule the new task
    task = asyncio.create_task(other_task())
    task2 = asyncio.create_task(task)
    # do some other blocking things
    await asyncio.sleep(0)
    # get the result from by other task
    # result = task.result()
    # report the result
    # print(result)
    print('End')
 
# start the asyncio program
asyncio.run(main())