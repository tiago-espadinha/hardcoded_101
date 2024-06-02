import asyncio
import time

async def slow_task(duration, name):
    print(f"Task {name} starting (duration {duration}s)")
    await asyncio.sleep(duration)
    print(f"Task {name} finished")
    return f"{name} result"

async def demo_wait_for():
    print("\n--- asyncio.wait_for ---")
    try:
        # Task that takes 5 seconds, but timeout is 2
        await asyncio.wait_for(slow_task(5, "Slow"), timeout=2.0)
    except asyncio.TimeoutError:
        print("Slow task timed out as expected")

async def demo_shield():
    print("\n--- asyncio.shield ---")
    # shield protects a task from being cancelled even if the await is cancelled
    task = asyncio.create_task(slow_task(3, "Shielded"))
    shielded = asyncio.shield(task)
    
    try:
        await asyncio.wait_for(shielded, timeout=1.0)
    except asyncio.TimeoutError:
        print("Wait for shielded task timed out, but task continues in background")
        await task
        print("Shielded task finally finished")

async def demo_task_group():
    print("\n--- asyncio.TaskGroup (Python 3.11+) ---")
    try:
        async with asyncio.TaskGroup() as tg:
            t1 = tg.create_task(slow_task(1, "TG-1"))
            t2 = tg.create_task(slow_task(2, "TG-2"))
            print("Both tasks started in TaskGroup")
        print(f"TaskGroup results: {t1.result()}, {t2.result()}")
    except Exception as e:
        print(f"TaskGroup error: {e}")

class AsyncCM:
    async def __aenter__(self):
        print("Entering Async Context")
        await asyncio.sleep(0.1)
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        print("Exiting Async Context")
        await asyncio.sleep(0.1)

async def demo_async_gen():
    print("\n--- Async Generators ---")
    async def async_gen():
        for i in range(3):
            await asyncio.sleep(0.1)
            yield i
            
    async for val in async_gen():
        print(f"Received from async gen: {val}")

async def main():
    await demo_wait_for()
    await demo_shield()
    await demo_task_group()
    
    print("\n--- Async Context Manager ---")
    async with AsyncCM():
        print("Inside context manager")
        
    await demo_async_gen()

if __name__ == "__main__":
    asyncio.run(main())
