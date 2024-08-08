#ifndef THREAD_POOL_H
#define THREAD_POOL_H

typedef struct ThreadPool ThreadPool;

ThreadPool *tp_create(int num_threads);
int         tp_submit(ThreadPool *tp, void (*fn)(void*), void *arg);
void        tp_destroy(ThreadPool *tp);

#endif
