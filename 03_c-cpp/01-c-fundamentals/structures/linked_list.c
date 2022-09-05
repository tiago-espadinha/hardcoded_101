/*
 * linked_list.c — Singly linked list implementation with demo main().
 *
 * Compile:
 *   gcc -std=c17 -Wall -Wextra -Werror -fsanitize=address,undefined \
 *       -o linked_list linked_list.c
 */

#include "linked_list.h"

#include <stdio.h>
#include <stdlib.h>

/* ── internal helper ──────────────────────────────────────────────────────── */

static Node *create_node(int value) {
    Node *n = malloc(sizeof(Node));
    if (!n) { perror("malloc node"); exit(EXIT_FAILURE); }
    n->data = value;
    n->next = NULL;
    return n;
}

/* ── lifecycle ────────────────────────────────────────────────────────────── */

void ll_init(LinkedList *ll) {
    if (!ll) return;
    ll->head = NULL;
    ll->size = 0;
}

void ll_free(LinkedList *ll) {
    if (!ll) return;
    Node *cur = ll->head;
    while (cur) {
        Node *next = cur->next;
        free(cur);
        cur = next;
    }
    ll->head = NULL;
    ll->size = 0;
}

/* ── mutation ─────────────────────────────────────────────────────────────── */

/* O(n) */
void ll_append(LinkedList *ll, int value) {
    if (!ll) return;
    Node *n = create_node(value);
    if (!ll->head) {
        ll->head = n;
    } else {
        Node *cur = ll->head;
        while (cur->next) cur = cur->next;
        cur->next = n;
    }
    ll->size++;
}

/* O(1) */
void ll_prepend(LinkedList *ll, int value) {
    if (!ll) return;
    Node *n = create_node(value);
    n->next  = ll->head;
    ll->head = n;
    ll->size++;
}

/* O(n) — returns 1 if deleted, 0 if not found */
int ll_delete(LinkedList *ll, int value) {
    if (!ll || !ll->head) return 0;

    /* special case: value is in the head node */
    if (ll->head->data == value) {
        Node *old = ll->head;
        ll->head  = old->next;
        free(old);
        ll->size--;
        return 1;
    }

    Node *prev = ll->head;
    Node *cur  = prev->next;
    while (cur) {
        if (cur->data == value) {
            prev->next = cur->next;
            free(cur);
            ll->size--;
            return 1;
        }
        prev = cur;
        cur  = cur->next;
    }
    return 0;  /* not found */
}

/* O(n) */
void ll_reverse(LinkedList *ll) {
    if (!ll) return;
    Node *prev = NULL;
    Node *cur  = ll->head;
    while (cur) {
        Node *next = cur->next;
        cur->next  = prev;
        prev       = cur;
        cur        = next;
    }
    ll->head = prev;
}

/* ── query ────────────────────────────────────────────────────────────────── */

/* O(n) */
Node *ll_search(const LinkedList *ll, int value) {
    if (!ll) return NULL;
    Node *cur = ll->head;
    while (cur) {
        if (cur->data == value) return cur;
        cur = cur->next;
    }
    return NULL;
}

/* O(n) — caller must free() the returned array */
int *ll_to_array(const LinkedList *ll) {
    if (!ll || ll->size == 0) return NULL;
    int *arr = malloc(ll->size * sizeof(int));
    if (!arr) { perror("malloc to_array"); return NULL; }
    Node *cur = ll->head;
    for (size_t i = 0; i < ll->size; i++, cur = cur->next) {
        arr[i] = cur->data;
    }
    return arr;
}

/* O(1) */
size_t ll_size(const LinkedList *ll) {
    return ll ? ll->size : 0;
}

/* ── display ──────────────────────────────────────────────────────────────── */

void ll_print(const LinkedList *ll) {
    printf("  head");
    if (!ll) { printf(" -> (null list)\n"); return; }
    Node *cur = ll->head;
    while (cur) {
        printf(" -> %d", cur->data);
        cur = cur->next;
    }
    printf(" -> NULL  (size=%zu)\n", ll->size);
}

/* ── demo main ────────────────────────────────────────────────────────────── */

static void section(const char *title) {
    printf("\n===== %s =====\n", title);
}

int main(void) {
    printf("==========================================================\n");
    printf("  Singly Linked List Demo\n");
    printf("==========================================================\n");

    LinkedList ll;
    ll_init(&ll);

    section("append 1..5");
    for (int i = 1; i <= 5; i++) ll_append(&ll, i * 10);
    ll_print(&ll);

    section("prepend 0");
    ll_prepend(&ll, 0);
    ll_print(&ll);

    section("search");
    Node *found = ll_search(&ll, 30);
    printf("  search(30): %s\n", found ? "found" : "not found");
    found = ll_search(&ll, 99);
    printf("  search(99): %s\n", found ? "found" : "not found");

    section("delete middle (30), head (0), tail (50)");
    ll_delete(&ll, 30);
    ll_delete(&ll, 0);
    ll_delete(&ll, 50);
    ll_print(&ll);

    section("reverse");
    ll_reverse(&ll);
    ll_print(&ll);

    section("to_array");
    int *arr = ll_to_array(&ll);
    printf("  [");
    for (size_t i = 0; i < ll_size(&ll); i++) {
        printf("%d%s", arr[i], i + 1 < ll_size(&ll) ? ", " : "");
    }
    printf("]\n");
    free(arr);

    section("delete all — should not leak");
    while (ll.head) ll_delete(&ll, ll.head->data);
    ll_print(&ll);

    ll_free(&ll);
    printf("\nDone.\n");
    return 0;
}
