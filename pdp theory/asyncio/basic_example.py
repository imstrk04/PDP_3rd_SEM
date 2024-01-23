import asyncio

async def task(name, duration):
    print(f"Task {name} started, sleeping for {duration} seconds.")
    await asyncio.sleep(duration)
    print(f"Task {name} completed.")

async def main():
    tasks = [
        task("A", 2),
        task("B",1),
        task("C", 3),
    ]

    await asyncio.gather(*tasks)

asyncio.run(main())

