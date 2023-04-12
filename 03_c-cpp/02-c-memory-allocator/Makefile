CC = gcc
CFLAGS = -std=c17 -Wall -Wextra -Werror


BENCHMARKS = benchmark_first benchmark_best benchmark_buddy
TESTS = test_corr_first test_corr_best test_corr_buddy test_frags_first test_frags_best test_frags_buddy

.PHONY: all benchmarks tests clean

all: $(BENCHMARKS) $(TESTS)

# Compile and run all benchmarks
benchmarks: $(BENCHMARKS)
	./benchmark_first
	./benchmark_best
	./benchmark_buddy

# Compile and run all tests
tests: $(TESTS)
	./test_corr_first
	./test_corr_best
	./test_corr_buddy
	./test_frags_first
	./test_frags_best
	./test_frags_buddy

# --------------------
# Benchmarks
# --------------------

benchmark_first: benchmark.c first_fit.c
	$(CC) $(CFLAGS) benchmark.c first_fit.c -o benchmark_first

benchmark_best: benchmark.c best_fit.c
	$(CC) $(CFLAGS) benchmark.c best_fit.c -o benchmark_best

benchmark_buddy: benchmark.c buddy.c
	$(CC) $(CFLAGS) benchmark.c buddy.c -o benchmark_buddy


# --------------------
# Tests
# --------------------

test_corr_first: tests/test_correctness.c first_fit.c
	$(CC) $(CFLAGS) tests/test_correctness.c first_fit.c -o test_corr_first

test_corr_best: tests/test_correctness.c best_fit.c
	$(CC) $(CFLAGS) tests/test_correctness.c best_fit.c -o test_corr_best

test_corr_buddy: tests/test_correctness.c buddy.c
	$(CC) $(CFLAGS) tests/test_correctness.c buddy.c -o test_corr_buddy

test_frags_first: tests/test_fragmentation.c first_fit.c
	$(CC) $(CFLAGS) tests/test_fragmentation.c first_fit.c -o test_frags_first

test_frags_best: tests/test_fragmentation.c best_fit.c
	$(CC) $(CFLAGS) tests/test_fragmentation.c best_fit.c -o test_frags_best

test_frags_buddy: tests/test_fragmentation.c buddy.c
	$(CC) $(CFLAGS) tests/test_fragmentation.c buddy.c -o test_frags_buddy

# --------------------
# Clean
# --------------------

clean:
	rm -f benchmark_first benchmark_best benchmark_buddy \
	      test_corr_first test_corr_best test_corr_buddy test_frags_first test_frags_best test_frags_buddy *.o