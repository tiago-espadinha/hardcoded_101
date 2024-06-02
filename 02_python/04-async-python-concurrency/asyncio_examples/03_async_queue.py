import asyncio
import random
import time

async def producer(name, queue, num_items):
    print(f"Producer {name} starting...")
    for i in range(num_items):
        # Simulate work
        item = f"item-{name}-{i}"
        await asyncio.sleep(random.random() * 0.2)
        
        # Put item in queue (will block if queue is full)
        print(f"Producer {name} putting {item} in queue (Queue size: {queue.qsize()})")
        await queue.put(item)
    print(f"Producer {name} finished.")

async def consumer(name, queue):
    print(f"Consumer {name} starting...")
    while True:
        # Get item from queue (will block if queue is empty)
        item = await queue.get()
        print(f"Consumer {name} processing {item} (Queue size: {queue.qsize()})")
        
        # Simulate processing work
        await asyncio.sleep(random.random() * 0.5)
        
        # Signal that the item has been processed
        queue.task_done()
        print(f"Consumer {name} finished {item}")

async def main():
    # Queue with backpressure (max 5 items)
    queue = asyncio.Queue(maxsize=5)
    
    # Launch producers and consumers
    producers = [asyncio.create_task(producer(f"P{i}", queue, 10)) for i in range(2)]
    consumers = [asyncio.create_task(consumer(f"C{i}", queue)) for i in range(3)]
    
    # Wait for all producers to finish
    await asyncio.gather(*producers)
    
    # Wait for all items in the queue to be processed
    await queue.join()
    
    # Cancel consumers (they would run forever)
    for c in consumers:
        c.cancel()
    
    print("All tasks completed.")

if __name__ == "__main__":
    asyncio.run(main())
