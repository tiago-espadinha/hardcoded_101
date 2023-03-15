CC = gcc
CFLAGS = -std=c17 -Wall -Wextra -Werror


BENCHMARKS = benchmark_first 
TESTS = test_corr_first test_frags_first 

.PHONY: all benchmarks tests clean

all: $(BENCHMARKS) $(TESTS)

# Compile and run all benchmarks
benchmarks: $(BENCHMARKS)
	./benchmark_first

# Compile and run all tests
tests: $(TESTS)
	./test_corr_first
	./test_frags_first


# --------------------
# Benchmarks
# --------------------

benchmark_first: benchmark.c first_fit.c
	$(CC) $(CFLAGS) benchmark.c first_fit.c -o benchmark_first


# --------------------
# Tests
# --------------------

test_corr_first: tests/test_correctness.c first_fit.c
	$(CC) $(CFLAGS) tests/test_correctness.c first_fit.c -o test_corr_first

test_frags_first: tests/test_fragmentation.c first_fit.c
	$(CC) $(CFLAGS) tests/test_fragmentation.c first_fit.c -o test_frags_first

# --------------------
# Clean
# --------------------

clean:
	rm -f benchmark_first benchmark_best benchmark_buddy \
	      test_corr_first test_frags_first *.o