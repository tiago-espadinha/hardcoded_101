CC = gcc
CFLAGS = -std=c17 -Wall -Wextra -Werror

SRC_FIRST = first_fit.c
SRC_BEST = best_fit.c
SRC_BUDDY = buddy.c

TEST_CORRECTNESS = tests/test_correctness.c
TEST_FRAG = tests/test_fragmentation.c
BENCHMARK = benchmark.c

all: benchmark test

benchmark: benchmark.c
	$(CC) $(CFLAGS) benchmark.c -o benchmark

test: test_correctness test_fragmentation

test_correctness: $(TEST_CORRECTNESS)
	$(CC) $(CFLAGS) $(TEST_CORRECTNESS) -o tests/test_correctness

test_fragmentation: $(TEST_FRAG)
	$(CC) $(CFLAGS) $(TEST_FRAG) -o tests/test_fragmentation

clean:
	rm -f tests/test_correctness tests/test_fragmentation benchmark *.o
