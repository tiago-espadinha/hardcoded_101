CC      = gcc
CSTD    = -std=c17
WARN    = -Wall -Wextra -Werror
ASAN    = -fsanitize=address,undefined
DBGFLG  = -g $(ASAN)
RELFLG  = -O2

# Export so sub-makes and scripts inherit the chosen flags
export CC CSTD WARN

# ── source lists ───────────────────────────────────────────────────────────

MEM_SRCS = memory/01_pointers.c \
           memory/02_stack_vs_heap.c \
           memory/03_pointers_and_arrays.c \
           memory/04_strings.c \
           memory/05_structs.c

MEM_BINS = $(MEM_SRCS:.c=)

STRUCT_SRCS = structures/linked_list.c \
              structures/hash_table.c

# linked_list.c has its own main; hash_table.c has its own main
STRUCT_BINS = structures/linked_list \
              structures/hash_table

FILES_SRCS = files/grade_tracker.c \
             files/binary_rw.c

FILES_BINS = $(FILES_SRCS:.c=)

ALL_BINS = $(MEM_BINS) $(STRUCT_BINS) $(FILES_BINS)

# ── default target ──────────────────────────────────────────────────────────

.PHONY: all debug release clean test

all: debug

# ── debug build (ASan + UBSan) ──────────────────────────────────────────────

debug: CFLAGS = $(CSTD) $(WARN) $(DBGFLG)
debug: $(ALL_BINS)

# ── release build (optimised) ───────────────────────────────────────────────

release: CFLAGS = $(CSTD) $(WARN) $(RELFLG)
release: $(ALL_BINS)

# ── pattern rules ───────────────────────────────────────────────────────────

# Memory module — single-file binaries
memory/%: memory/%.c
	$(CC) $(CFLAGS) -o $@ $<

# Structures — each needs its header sibling
structures/linked_list: structures/linked_list.c structures/linked_list.h
	$(CC) $(CFLAGS) -o $@ structures/linked_list.c

structures/hash_table: structures/hash_table.c structures/hash_table.h
	$(CC) $(CFLAGS) -o $@ structures/hash_table.c

# Files module — single-file binaries
files/%: files/%.c
	$(CC) $(CFLAGS) -o $@ $<

# ── test target ─────────────────────────────────────────────────────────────

test: debug
	@bash tests/run_tests.sh

# ── clean ────────────────────────────────────────────────────────────────────

clean:
	rm -f $(ALL_BINS)
	rm -f files/students.csv files/data.bin files/data.txt
	@echo "Cleaned."
