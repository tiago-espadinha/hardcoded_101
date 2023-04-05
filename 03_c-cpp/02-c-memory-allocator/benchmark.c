#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "allocator.h"

#define NUM_ALLOCS 10000

void run_benchmark(const char *name) {
    printf("Benchmarking %s...\n", name);
    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);

    void *ptrs[NUM_ALLOCS];
    for (int i = 0; i < NUM_ALLOCS; i++) {
        ptrs[i] = myalloc((rand() % 128) + 8);
    }

    for (int i = 0; i < NUM_ALLOCS; i++) {
        myfree(ptrs[i]);
    }

    clock_gettime(CLOCK_MONOTONIC, &end);
    double time_taken = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
    printf("%s took %f seconds\n", name, time_taken);
}

int main(int argc, char *argv[]) {
    if (argc != 0){
        char benchmark[256];
        snprintf(benchmark, sizeof(benchmark), "%s Allocator", argv[0]);
        run_benchmark(benchmark);
        printf("\n");
    }
    return 0;
}
