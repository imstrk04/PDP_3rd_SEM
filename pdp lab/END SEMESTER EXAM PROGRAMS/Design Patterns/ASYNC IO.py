import asyncio
import time 
async def brew_coffee():
    print('Start making coffee')
    await asyncio.sleep(2)
    print('Coffee made')

async def bake_pastry():
    print('Start baking')
    await asyncio.sleep(1)
    print('Pastry made')

async def main():
    start_time=time.time()
    # Call the coroutine functions with parentheses
    task1 = asyncio.create_task(brew_coffee())
    task2 = asyncio.create_task(bake_pastry())

    # Wait for tasks to complete
    await asyncio.gather(task1, task2)
    end_time=time.time()

    runtime=end_time-start_time
    print(runtime)

# Run the event loop using asyncio.run with the main coroutine
asyncio.run(main())

'''in this case we get the run time as 2.0489593465689436894
now if we try without asyncio the same program we get '''

import time

def brew_coffee():
    print('Start making coffee')
    time.sleep(2)
    print('Coffee made')

def bake_pastry():
    print('Start baking')
    time.sleep(1)
    print('Pastry made')

def main():
    start_time = time.time()

    # Call the functions synchronously
    brew_coffee()
    bake_pastry()

    end_time = time.time()
    runtime = end_time - start_time
    print(f"Total runtime: {runtime} seconds")

# Run the program synchronously
main()

''' in this case we get 3.1160006523132324 seconds as run time '''
