#include <stdio.h>
#include <stdlib.h>
#include "../allocator.h"

void test_fragmentation(const char *name) {
    printf("Running fragmentation test for %s...\n", name);
    void *ptrs[1000];
    for (int i = 0; i < 1000; i++) {
        ptrs[i] = myalloc(8);
    }

    for (int i = 0; i < 1000; i += 2) {
        myfree(ptrs[i]);
    }

    void *large = myalloc(64);
    if (large) {
        printf("64-byte allocation succeeded despite fragmentation!\n");
        myfree(large);
    } else {
        printf("64-byte allocation failed as expected (external fragmentation).\n");
    }

    // Since we don't have a way to inspect the free list size from allocator.h,
    // we just print that it succeeded/failed.
}

int main(int argc, char *argv[]) {
    if (argc != 0){
        char benchmark[256];
        snprintf(benchmark, sizeof(benchmark), "%s Allocator", argv[0]);
        test_fragmentation(benchmark);
        printf("\n");
    }
    return 0;
}
