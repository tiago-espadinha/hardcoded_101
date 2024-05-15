import threading
import queue
import time
import random

class Message:
    def __init__(self, topic, payload):
        self.topic = topic
        self.payload = payload
        self.retry_count = 0

class InMemoryQueue:
    def __init__(self):
        self.topics = {}
        self.lock = threading.Lock()
        self.dead_letter_queue = []

    def publish(self, topic, payload):
        with self.lock:
            if topic not in self.topics:
                self.topics[topic] = []
            message = Message(topic, payload)
            self.topics[topic].append(message)
            print(f"Published to {topic}: {payload}")

    def subscribe(self, topic, callback):
        def worker():
            while True:
                message = None
                with self.lock:
                    if topic in self.topics and len(self.topics[topic]) > 0:
                        message = self.topics[topic].pop(0)
                
                if message:
                    try:
                        # Attempt to deliver the message
                        callback(message.payload)
                        # Acknowledge: successfully processed
                    except Exception as e:
                        # Negative acknowledgement: failed to process
                        message.retry_count += 1
                        if message.retry_count >= 3:
                            print(f"Message {message.payload} failed 3 times. Moving to DLQ.")
                            with self.lock:
                                self.dead_letter_queue.append(message)
                        else:
                            print(f"Message {message.payload} failed. Retrying ({message.retry_count}/3)...")
                            # Put back into the queue for retry (at-least-once delivery)
                            with self.lock:
                                self.topics[topic].append(message)
                
                time.sleep(0.01) # Small sleep to prevent CPU spinning

        thread = threading.Thread(target=worker, daemon=True)
        thread.start()
        return thread
