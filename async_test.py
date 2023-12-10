import asyncio


async def print_number():
    number = 0
    while True:
        print(number)
        number += 1
        await asyncio.sleep(3)


async def print_letter():
    while True:
        print('a')
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_number())
    task2 = asyncio.create_task(print_letter())
    await task1
    await task2


asyncio.run(main())
