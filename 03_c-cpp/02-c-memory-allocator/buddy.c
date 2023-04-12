#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include "allocator.h"

#define HEAP_SIZE (32 * 1024 * 1024)
#define MIN_ALLOC 32

static char heap[HEAP_SIZE];

// In a real buddy system, we'd use free lists for each power of 2.
// For this implementation, we'll use a simple recursive approach or a header-based one.
// Let's use a header-based one for simplicity in this context.

typedef struct Block {
    size_t size; // Power of 2
    int free;
} Block;

static bool initialized = false;

static void init_heap() {
    Block *root = (Block *)heap;
    root->size = HEAP_SIZE;
    root->free = 1;
    initialized = true;
}

static size_t next_pow2(size_t n) {
    if (n < MIN_ALLOC) return MIN_ALLOC;
    n--;
    n |= n >> 1;
    n |= n >> 2;
    n |= n >> 4;
    n |= n >> 8;
    n |= n >> 16;
    n++;
    return n;
}

void *myalloc(size_t size) {
    if (size == 0) return NULL;
    if (!initialized) init_heap();

    size_t required = next_pow2(size + sizeof(Block));
    
    // Search for a free block
    uintptr_t offset = 0;
    while (offset < HEAP_SIZE) {
        Block *b = (Block *)(heap + offset);
        if (b->free && b->size >= required) {
            // Split if necessary
            while (b->size > required) {
                b->size /= 2;
                Block *buddy = (Block *)(heap + offset + b->size);
                buddy->size = b->size;
                buddy->free = 1;
            }
            b->free = 0;
            return (void *)((char *)b + sizeof(Block));
        }
        offset += b->size;
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

    // Coalesce buddies
    bool changed = true;
    while (changed) {
        changed = false;
        uintptr_t offset = 0;
        while (offset < HEAP_SIZE) {
            Block *b = (Block *)(heap + offset);
            uintptr_t buddy_offset = offset ^ b->size;
            if (buddy_offset < HEAP_SIZE) {
                Block *buddy = (Block *)(heap + buddy_offset);
                if (b->free && buddy->free && b->size == buddy->size) {
                    if (buddy_offset < offset) {
                        buddy->size *= 2;
                        offset = buddy_offset;
                    } else {
                        b->size *= 2;
                    }
                    changed = true;
                    break;
                }
            }
            offset += b->size;
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
    if (block->size >= size + sizeof(Block)) return ptr;

    void *new_ptr = myalloc(size);
    if (new_ptr) {
        memcpy(new_ptr, ptr, block->size - sizeof(Block));
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
