#ifndef ALLOCATOR_H
#define ALLOCATOR_H

#include <stddef.h>
#include <stdbool.h>

void *myalloc(size_t size);
void  myfree(void *ptr);
void *myrealloc(void *ptr, size_t size);
void *mycalloc(size_t nmemb, size_t size);

#endif
