#include <stdio.h>
#include <string.h>
#include "allocator.h"

#define HEAP_SIZE (32 * 1024 * 1024)
#define ALIGNMENT 8
#define ALIGN(size) (((size) + (ALIGNMENT - 1)) & ~(ALIGNMENT - 1))

typedef struct Block {
    size_t size;
    int free;
    struct Block *next;
} Block;

static char heap[HEAP_SIZE];
static Block *free_list = (Block *)heap;

static bool initialized = false;

static void init_heap() {
    free_list->size = HEAP_SIZE - sizeof(Block);
    free_list->free = 1;
    free_list->next = NULL;
    initialized = true;
}

void *myalloc(size_t size) {
    if (size == 0) return NULL;
    if (!initialized) init_heap();

    size = ALIGN(size);
    Block *best_block = NULL;
    Block *current = free_list;

    while (current) {
        if (current->free && current->size >= size) {
            if (!best_block || current->size < best_block->size) {
                best_block = current;
            }
        }
        current = current->next;
    }

    if (best_block) {
        if (best_block->size >= size + sizeof(Block) + ALIGNMENT) {
            Block *next = (Block *)((char *)best_block + sizeof(Block) + size);
            next->size = best_block->size - size - sizeof(Block);
            next->free = 1;
            next->next = best_block->next;

            best_block->size = size;
            best_block->next = next;
        }
        best_block->free = 0;
        return (void *)((char *)best_block + sizeof(Block));
    }

    return NULL;
}

void myfree(void *ptr) {
    if (!ptr) return;

    Block *block = (Block *)((char *)ptr - sizeof(Block));
    if ((char *)block < heap || (char *)block >= heap + HEAP_SIZE) {
        fprintf(stderr, "Error: myfree of non-allocated pointer\n");
        return;
    }

    block->free = 1;

    // Coalesce
    Block *current = free_list;
    while (current) {
        if (current->free && current->next && current->next->free) {
            current->size += current->next->size + sizeof(Block);
            current->next = current->next->next;
        } else {
            current = current->next;
        }
    }
}

void *myrealloc(void *ptr, size_t size) {
    if (!ptr) return myalloc(size);
    if (size == 0) {
        myfree(ptr);
        return NULL;
    }

    Block *block = (Block *)((char *)ptr - sizeof(Block));
    if (block->size >= size) return ptr;

    void *new_ptr = myalloc(size);
    if (new_ptr) {
        memcpy(new_ptr, ptr, block->size);
        myfree(ptr);
    }
    return new_ptr;
}

void *mycalloc(size_t nmemb, size_t size) {
    size_t total = nmemb * size;
    void *ptr = myalloc(total);
    if (ptr) memset(ptr, 0, total);
    return ptr;
}
