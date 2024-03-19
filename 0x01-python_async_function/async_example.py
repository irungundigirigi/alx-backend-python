""" https://www.youtube.com/watch?v=K56nNuBEd0c
"""
#!/usr/bin/env python3

import asyncio
import time

async def brewCoffee():
    print("brewCoffee() start")
    await asyncio.sleep(3)
    return "Coffee ready"

async def toastBagel():
    print("Start toastBagel()")
    await asyncio.sleep(2)
    return "Bagel toated"

async def main():
    start_time = time.time()
    coffee_task = asyncio.create_task(brewCoffee())
    bagel_task = asyncio.create_task(toastBagel())

    coffee = await coffee_task
    bagel = await bagel_task
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f'elapsed time : {elapsed_time}')

if __name__ == "__main__":
    asyncio.run(main())
