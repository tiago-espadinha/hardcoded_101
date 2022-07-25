/*
 * linked_list.h — Singly linked list interface.
 *
 * All functions handle NULL gracefully (empty list or value not found).
 */

#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <stddef.h>  /* size_t */

/* ── Node ──────────────────────────────────────────────────────────────────── */

typedef struct Node {
    int          data;
    struct Node *next;
} Node;

/* ── LinkedList ────────────────────────────────────────────────────────────── */

typedef struct {
    Node  *head;
    size_t size;
} LinkedList;

/* ── lifecycle ──────────────────────────────────────────────────────────────── */

/* Initialise a list in-place (does NOT allocate the LinkedList itself). */
void ll_init(LinkedList *ll);

/* Free all nodes; resets head and size. */
void ll_free(LinkedList *ll);

/* ── mutation ────────────────────────────────────────────────────────────────  */

/* O(n) — append value at the tail. */
void ll_append(LinkedList *ll, int value);

/* O(1) — insert value at the head. */
void ll_prepend(LinkedList *ll, int value);

/*
 * O(n) — remove the first node with matching value.
 * Does nothing if value is not in the list.
 * Returns 1 if removed, 0 if not found.
 */
int ll_delete(LinkedList *ll, int value);

/* O(n) — reverse the list in-place. */
void ll_reverse(LinkedList *ll);

/* ── query ───────────────────────────────────────────────────────────────────  */

/* O(n) — return pointer to first Node with matching value, or NULL. */
Node *ll_search(const LinkedList *ll, int value);

/* O(n) — copy list data into a newly malloc'd array; caller must free(). */
int  *ll_to_array(const LinkedList *ll);

/* O(1) — current number of nodes. */
size_t ll_size(const LinkedList *ll);

/* ── display ─────────────────────────────────────────────────────────────────  */

/* O(n) — print: head -> 1 -> 2 -> 3 -> NULL */
void ll_print(const LinkedList *ll);

#endif /* LINKED_LIST_H */
