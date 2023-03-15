#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../allocator.h"

void test_random_allocations(const char *name)
{
    printf("Running random allocations test for %s...\n", name);
    void *ptrs[1000];
    size_t sizes[1000];

    for (int i = 0; i < 1000; i++) {
        sizes[i] = (rand() % 4096) + 1;
        ptrs[i] = myalloc(sizes[i]);

        if (ptrs[i]) {
            memset(ptrs[i], 0xAA, sizes[i]);
        }
    }

    for (int i = 0; i < 500; i++) {
        if (ptrs[i]) {
            myfree(ptrs[i]);
            ptrs[i] = NULL;
        }
    }

    for (int i = 500; i < 1000; i++) {
        if (ptrs[i]) {
            unsigned char *p = ptrs[i];
            for (size_t j = 0; j < sizes[i]; j++) {
                if (p[j] != 0xAA) {
                    printf(
                        "Corruption detected at ptr[%d], byte %zu!\n",
                        i,
                        j
                    );
                    return;
                }
            }
        }
    }

    for (int i = 500; i < 1000; i++) {
        if (ptrs[i]) {
            myfree(ptrs[i]);
        }
    }

    printf("Random allocations test passed.\n");
}

void test_realloc(const char *name) {
    printf("Running realloc test for %s...\n", name);
    void *ptr = myalloc(10);
    memset(ptr, 0xBB, 10);
    ptr = myrealloc(ptr, 20);
    unsigned char *p = (unsigned char *)ptr;
    if (p[0] != 0xBB) {
        printf("Realloc data not preserved!\n");
        return;
    }
    myfree(ptr);
    printf("Realloc test passed.\n");
}

int main(int argc, char *argv[]) {
    if (argc != 0){
        char test_name[256];
        snprintf(test_name, sizeof(test_name), "%s Allocator", argv[0]);
        test_random_allocations(test_name);
        test_realloc(test_name);
        printf("\n");
    }
    myfree(NULL); // Should not crash
    return 0;
}
