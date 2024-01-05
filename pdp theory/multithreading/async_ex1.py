import asyncio

async def do_fun(i = 0) -> None:
     print(f"I am  {i}")
     await asyncio.sleep(3)
     print(f"I WOKE UP {i}")
    

async def thrdcreation(count = 5)-> None:
    print("will do multi tasking now")
    
    tasks = [asyncio.create_task(do_fun(i)) for i in range (3) ]
    print("hi")
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(thrdcreation(5))
print("Done with the sleepers")

    

