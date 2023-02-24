import asyncio
from typing import Callable, Dict, List, Any, TypeVar, Generic

T = TypeVar("T")

class EventEmitter(Generic[T]):
    """An event system (EventEmitter) with typed events and async callbacks."""
    
    def __init__(self):
        self._listeners: Dict[str, List[Callable[[T], Any]]] = {}

    def on(self, event_name: str, callback: Callable[[T], Any]):
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append(callback)

    def off(self, event_name: str, callback: Callable[[T], Any]):
        if event_name in self._listeners:
            self._listeners[event_name].remove(callback)

    async def emit(self, event_name: str, data: T):
        if event_name in self._listeners:
            tasks = []
            for callback in self._listeners[event_name]:
                if asyncio.iscoroutinefunction(callback):
                    tasks.append(callback(data))
                else:
                    callback(data)
            
            if tasks:
                await asyncio.gather(*tasks)

# Example usage
async def main():
    emitter = EventEmitter[dict]()

    def sync_logger(data):
        print(f"Sync Logger: Received event with data: {data}")

    async def async_processor(data):
        await asyncio.sleep(0.5)
        print(f"Async Processor: Processed data: {data}")

    emitter.on("user_signup", sync_logger)
    emitter.on("user_signup", async_processor)

    print("Emitting 'user_signup' event...")
    await emitter.emit("user_signup", {"user": "alice", "email": "alice@example.com"})
    print("Event emission finished.")

if __name__ == "__main__":
    asyncio.run(main())
