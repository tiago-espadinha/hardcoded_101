"""
Demonstrates collections in Python.
Covers: Counter, defaultdict, OrderedDict, namedtuple, deque
"""
from collections import Counter, defaultdict, namedtuple, deque

def main():
    # Counter
    c = Counter("abracadabra")
    print(f"Counter: {c}")
    print(f"Top 3: {c.most_common(3)}")

    # defaultdict
    d = defaultdict(list)
    d["fruits"].append("apple")
    d["fruits"].append("banana")
    print(f"defaultdict: {d}")

    # namedtuple
    Point = namedtuple("Point", ["x", "y"])
    p = Point(10, 20)
    print(f"Point: {p}, x={p.x}, y={p.y}")

    # deque
    q = deque(["a", "b", "c"])
    q.append("d")
    q.appendleft("z")
    print(f"Deque: {q}")
    print(f"Pop: {q.pop()}, Popleft: {q.popleft()}")

if __name__ == "__main__":
    main()
