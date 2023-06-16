import asyncio
import time

async def sleep():
    await asyncio.sleep(1)

async def num_check(num):
    start = time.time()
    for i in range(1, num):
        print(i)
        await sleep()
    
    end = time.time()
    print(end - start)

async def main():

    start = time.time()    
    res1 = asyncio.create_task(num_check(5))
    res2 = asyncio.create_task(num_check(5))

    await res1
    await res2

    res_t1 = res1.result()
    res_t2 = res2.result()

    end = time.time()

    print(f'총 시간 = {end - start}')

if __name__ == "__main__":
    asyncio.run(main(), debug=True)