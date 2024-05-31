from message_queue import InMemoryQueue
import time
import random

def main():
    mq = InMemoryQueue()
    processed_count = 0
    failed_count = 0

    def consumer_callback(payload, consumer_id):
        nonlocal processed_count, failed_count
        # Consumer 1 (ID 1) randomly fails 30% of the time
        if consumer_id == 1 and random.random() < 0.3:
            raise Exception("Random failure")
        
        print(f"Consumer {consumer_id} processed: {payload}")
        processed_count += 1

    # Subscribe 3 consumers
    mq.subscribe("topic1", lambda p: consumer_callback(p, 1))
    mq.subscribe("topic1", lambda p: consumer_callback(p, 2))
    mq.subscribe("topic1", lambda p: consumer_callback(p, 3))

    # Producer: send 100 messages
    print("Producer sending 100 messages...")
    for i in range(100):
        mq.publish("topic1", f"msg_{i}")

    # Wait for processing to complete
    time.sleep(5)
    
    print("\n--- Final Stats ---")
    print(f"Successfully processed messages: {processed_count}")
    print(f"Messages in Dead Letter Queue: {len(mq.dead_letter_queue)}")
    for dlq_msg in mq.dead_letter_queue:
        print(f" - Failed message: {dlq_msg.payload}")

if __name__ == "__main__":
    main()
