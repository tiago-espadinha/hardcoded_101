#include "thread_pool.h"
#include <pthread.h>
#include <stdlib.h>
#include <stdbool.h>

#define TASK_QUEUE_SIZE 256

typedef struct {
    void (*fn)(void*);
    void *arg;
} Task;

struct ThreadPool {
    pthread_t *threads;
    int num_threads;
    Task queue[TASK_QUEUE_SIZE];
    int head;
    int tail;
    int count;
    pthread_mutex_t lock;
    pthread_cond_t cond;
    bool stop;
};

static void *worker(void *arg) {
    ThreadPool *tp = (ThreadPool *)arg;
    while (true) {
        pthread_mutex_lock(&tp->lock);
        while (tp->count == 0 && !tp->stop) {
            pthread_cond_wait(&tp->cond, &tp->lock);
        }

        if (tp->stop && tp->count == 0) {
            pthread_mutex_unlock(&tp->lock);
            break;
        }

        Task task = tp->queue[tp->head];
        tp->head = (tp->head + 1) % TASK_QUEUE_SIZE;
        tp->count--;

        pthread_mutex_unlock(&tp->lock);
        task.fn(task.arg);
    }
    return NULL;
}

ThreadPool *tp_create(int num_threads) {
    ThreadPool *tp = malloc(sizeof(ThreadPool));
    tp->num_threads = num_threads;
    tp->threads = malloc(sizeof(pthread_t) * num_threads);
    tp->head = 0;
    tp->tail = 0;
    tp->count = 0;
    tp->stop = false;
    pthread_mutex_init(&tp->lock, NULL);
    pthread_cond_init(&tp->cond, NULL);

    for (int i = 0; i < num_threads; i++) {
        pthread_create(&tp->threads[i], NULL, worker, tp);
    }
    return tp;
}

int tp_submit(ThreadPool *tp, void (*fn)(void*), void *arg) {
    pthread_mutex_lock(&tp->lock);
    if (tp->count == TASK_QUEUE_SIZE) {
        pthread_mutex_unlock(&tp->lock);
        return -1;
    }
    tp->queue[tp->tail].fn = fn;
    tp->queue[tp->tail].arg = arg;
    tp->tail = (tp->tail + 1) % TASK_QUEUE_SIZE;
    tp->count++;
    pthread_cond_signal(&tp->cond);
    pthread_mutex_unlock(&tp->lock);
    return 0;
}

void tp_destroy(ThreadPool *tp) {
    pthread_mutex_lock(&tp->lock);
    tp->stop = true;
    pthread_cond_broadcast(&tp->cond);
    pthread_mutex_unlock(&tp->lock);

    for (int i = 0; i < tp->num_threads; i++) {
        pthread_join(tp->threads[i], NULL);
    }

    free(tp->threads);
    pthread_mutex_destroy(&tp->lock);
    pthread_cond_destroy(&tp->cond);
    free(tp);
}
