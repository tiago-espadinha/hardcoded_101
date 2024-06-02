import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return what

async def demo_sequential():
    print(f"Starting sequential at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"Finished sequential at {time.strftime('%X')}")

async def demo_gather():
    print(f"Starting gather at {time.strftime('%X')}")
    # Run concurrently
    results = await asyncio.gather(
        say_after(1, 'hello'),
        say_after(2, 'world')
    )
    print(f"Finished gather at {time.strftime('%X')}")
    print(f"Results: {results}")

async def demo_tasks():
    print(f"Starting tasks at {time.strftime('%X')}")
    # Create Tasks (schedules them immediately)
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    
    print("Tasks created, doing other work...")
    await asyncio.sleep(0.5)
    
    # Wait for completion
    await task1
    await task2
    print(f"Finished tasks at {time.strftime('%X')}")

if __name__ == "__main__":
    print("--- Asyncio Coroutines Demo ---")
    asyncio.run(demo_sequential())
    print("-" * 30)
    asyncio.run(demo_gather())
    print("-" * 30)
    asyncio.run(demo_tasks())
