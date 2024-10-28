import asyncio

async def start_strongmen(name, power):
    print(f'Силач {name} начал соревнования.')
    n = 1
    while n <= 5:
        await asyncio.sleep(10 / power)
        print(f"Силач {name} поднял {n} шар ")
        n += 1
    print(f'Силач {name} закончил соревнование')

async def main():
    participant1 = asyncio.create_task(start_strongmen("Pasha", 2))
    participant2 = asyncio.create_task(start_strongmen("Denis", 3))
    participant3 = asyncio.create_task(start_strongmen("Apolon", 5))

    await participant1
    await participant2
    await participant3


asyncio.run(main())


