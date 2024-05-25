import random
import string
from bloom_filter import BloomFilter

def random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

if __name__ == "__main__":
    bf = BloomFilter(capacity=10000, error_rate=0.01)
    
    # Insert 10k words
    words = [random_string() for _ in range(10000)]
    for word in words:
        bf.add(word)
    
    # Test 10k unseen words
    unseen_words = [random_string(11) for _ in range(10000)]
    false_positives = 0
    for word in unseen_words:
        if bf.might_contain(word):
            false_positives += 1
            
    print(f"Total inserted: 10,000")
    print(f"Total tested (unseen): 10,000")
    print(f"False Positives: {false_positives}")
    print(f"False Positive Rate: {false_positives / 10000 * 100:.2f}%")
