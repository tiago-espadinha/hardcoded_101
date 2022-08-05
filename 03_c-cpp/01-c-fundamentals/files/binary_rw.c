/*
 * binary_rw.c — Binary vs text file I/O benchmark.
 *
 * Writes 1 000 000 random ints to a binary file and a text file,
 * reads each back, verifies round-trip integrity, and compares:
 *   - File size (bytes)
 *   - Read time (clock ticks → milliseconds)
 *
 * Compile:
 *   gcc -std=c17 -Wall -Wextra -Werror -O2 -o binary_rw binary_rw.c
 *   (run with -O2; sanitizers slow clocks too much for a fair benchmark)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define N          1000000     /* number of integers */
#define SMALL_N    1000        /* smaller set for write demo */
#define BIN_FILE   "data.bin"
#define TXT_FILE   "data.txt"
#define SEED       20220802u

/* ── helpers ──────────────────────────────────────────────────────────────── */

static void print_separator(const char *title) {
    printf("\n===== %s =====\n", title);
}

/* lcg_rand — deterministic PRNG so results are reproducible. */
static unsigned int lcg_rand(unsigned int *state) {
    *state = *state * 1664525u + 1013904223u;
    return *state;
}

/* file_size_bytes — return the size of a file without reading it. */
static long file_size_bytes(const char *path) {
    FILE *f = fopen(path, "rb");
    if (!f) return -1;
    fseek(f, 0, SEEK_END);
    long sz = ftell(f);
    fclose(f);
    return sz;
}

/* elapsed_ms — convert two clock_t values to milliseconds. */
static double elapsed_ms(clock_t start, clock_t end) {
    return (double)(end - start) * 1000.0 / (double)CLOCKS_PER_SEC;
}

/* ── binary write / read ──────────────────────────────────────────────────── */

static void write_binary(const int *arr, size_t n, const char *path) {
    FILE *f = fopen(path, "wb");
    if (!f) { perror("fopen binary write"); exit(EXIT_FAILURE); }
    size_t written = fwrite(arr, sizeof(int), n, f);
    if (written != n) { fprintf(stderr, "Short write!\n"); exit(EXIT_FAILURE); }
    fclose(f);
}

/* Returns a heap-allocated array of n ints; caller must free(). */
static int *read_binary(const char *path, size_t n) {
    FILE *f = fopen(path, "rb");
    if (!f) { perror("fopen binary read"); exit(EXIT_FAILURE); }
    int *arr = malloc(n * sizeof(int));
    if (!arr) { perror("malloc"); exit(EXIT_FAILURE); }
    size_t got = fread(arr, sizeof(int), n, f);
    if (got != n) { fprintf(stderr, "Short read!\n"); exit(EXIT_FAILURE); }
    fclose(f);
    return arr;
}

/* ── text write / read ────────────────────────────────────────────────────── */

static void write_text(const int *arr, size_t n, const char *path) {
    FILE *f = fopen(path, "w");
    if (!f) { perror("fopen text write"); exit(EXIT_FAILURE); }
    for (size_t i = 0; i < n; i++) fprintf(f, "%d\n", arr[i]);
    fclose(f);
}

static int *read_text(const char *path, size_t n) {
    FILE *f = fopen(path, "r");
    if (!f) { perror("fopen text read"); exit(EXIT_FAILURE); }
    int *arr = malloc(n * sizeof(int));
    if (!arr) { perror("malloc"); exit(EXIT_FAILURE); }
    for (size_t i = 0; i < n; i++) {
        if (fscanf(f, "%d", &arr[i]) != 1) {
            fprintf(stderr, "Parse error at element %zu\n", i);
            exit(EXIT_FAILURE);
        }
    }
    fclose(f);
    return arr;
}

/* ── round-trip verification ─────────────────────────────────────────────── */

static int verify(const int *original, const int *recovered, size_t n) {
    return memcmp(original, recovered, n * sizeof(int)) == 0;
}

/* ── demo: inspect first few bytes of binary file ────────────────────────── */

static void demo_hex_dump(const char *path, size_t bytes) {
    FILE *f = fopen(path, "rb");
    if (!f) return;
    printf("  First %zu bytes of %s (raw hex):\n  ", bytes, path);
    for (size_t i = 0; i < bytes; i++) {
        int c = fgetc(f);
        if (c == EOF) break;
        printf("%02x ", (unsigned char)c);
        if ((i + 1) % 16 == 0) printf("\n  ");
    }
    printf("\n");
    fclose(f);
}

/* ── entry point ──────────────────────────────────────────────────────────── */

int main(void) {
    printf("==========================================================\n");
    printf("  binary_rw — Binary vs Text File I/O in C\n");
    printf("==========================================================\n");

    /* ── generate data ──────────────────────────────────────────────────── */
    print_separator("Generating data");
    unsigned int rng = SEED;

    int *original = malloc(N * sizeof(int));
    if (!original) { perror("malloc"); return 1; }
    for (size_t i = 0; i < N; i++)
        original[i] = (int)(lcg_rand(&rng) % 1000000);
    printf("  Generated %d integers (seed=%u).\n", N, SEED);

    /* ── small write demo ───────────────────────────────────────────────── */
    print_separator("Small write demo (first 1 000 values)");
    write_binary(original, SMALL_N, BIN_FILE);
    write_text(original, SMALL_N, TXT_FILE);

    printf("  Binary file size for %d ints: %ld bytes  "
           "(%zu bytes each — exact width)\n",
           SMALL_N, file_size_bytes(BIN_FILE), sizeof(int));
    printf("  Text   file size for %d ints: %ld bytes  "
           "(variable-width ASCII + newlines)\n",
           SMALL_N, file_size_bytes(TXT_FILE));

    demo_hex_dump(BIN_FILE, 32);

    /* ── full round-trip benchmark ──────────────────────────────────────── */
    print_separator("Round-trip benchmark — 1 000 000 integers";

    /* binary write + read */
    clock_t t0 = clock();
    write_binary(original, N, BIN_FILE);
    clock_t t1 = clock();
    int *bin_recovered = read_binary(BIN_FILE, N);
    clock_t t2 = clock();

    /* text write + read */
    clock_t t3 = clock();
    write_text(original, N, TXT_FILE);
    clock_t t4 = clock();
    int *txt_recovered = read_text(TXT_FILE, N);
    clock_t t5 = clock();

    printf("\n  %-14s  %-12s  %-12s  %-10s  %-8s\n",
           "Format", "Write (ms)", "Read (ms)", "Size (MB)", "Verified");
    printf("  %-14s  %-12s  %-12s  %-10s  %-8s\n",
           "--------------", "----------", "---------", "---------", "--------");
    printf("  %-14s  %-12.1f  %-12.1f  %-10.2f  %-8s\n",
           "Binary",
           elapsed_ms(t0, t1), elapsed_ms(t1, t2),
           (double)file_size_bytes(BIN_FILE) / 1e6,
           verify(original, bin_recovered, N) ? "OK" : "FAIL");
    printf("  %-14s  %-12.1f  %-12.1f  %-10.2f  %-8s\n",
           "Text",
           elapsed_ms(t3, t4), elapsed_ms(t4, t5),
           (double)file_size_bytes(TXT_FILE) / 1e6,
           verify(original, txt_recovered, N) ? "OK" : "FAIL");

    printf("\n  Binary is typically 4× smaller and 2–10× faster to read.\n");

    free(original);
    free(bin_recovered);
    free(txt_recovered);

    printf("\nDone.\n");
    return 0;
}
