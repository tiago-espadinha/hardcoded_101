/*
 * hash_table.c — Open-addressing hash table with linear probing.
 *
 * Compile:
 *   gcc -std=c17 -Wall -Wextra -Werror -fsanitize=address,undefined \
 *       -o hash_table hash_table.c
 */

#include "hash_table.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LOAD_FACTOR_MAX  0.70
#define INITIAL_CAPACITY 16

/* ── djb2 hash ────────────────────────────────────────────────────────────── */

/*
 * djb2 — Dan Bernstein's classic string hash.
 * Produces a size_t suitable for masking with (capacity - 1).
 * Time: O(n) where n = strlen(key)
 */
static size_t djb2(const char *key) {
    size_t hash = 5381;
    unsigned char c;
    while ((c = (unsigned char)*key++) != '\0')
        hash = ((hash << 5) + hash) ^ c;  /* hash * 33 XOR c */
    return hash;
}

/* ── internal helpers ─────────────────────────────────────────────────────── */

/* Round n up to the next power of two (minimum min_val). */
static size_t next_pow2(size_t n, size_t min_val) {
    size_t p = min_val;
    while (p < n) p <<= 1;
    return p;
}

/* Allocate a zeroed Slot array of 'cap' elements. */
static Slot *alloc_slots(size_t cap) {
    Slot *slots = calloc(cap, sizeof(Slot));
    if (!slots) { perror("calloc slots"); exit(EXIT_FAILURE); }
    return slots;
}

/*
 * probe — find the slot for 'key' in slots[0..cap-1].
 * Returns the index of the SLOT_OCCUPIED match, or the first SLOT_EMPTY
 * or SLOT_DELETED slot that can be used for insertion.
 */
static size_t probe(const Slot *slots, size_t cap, const char *key) {
    size_t idx       = djb2(key) & (cap - 1);
    size_t tombstone = (size_t)-1;

    for (size_t i = 0; i < cap; i++) {
        size_t pos = (idx + i) & (cap - 1);
        const Slot *s = &slots[pos];

        if (s->state == SLOT_EMPTY) {
            /* If we passed a tombstone, prefer it for insertion */
            return tombstone != (size_t)-1 ? tombstone : pos;
        }
        if (s->state == SLOT_DELETED) {
            if (tombstone == (size_t)-1) tombstone = pos;
            continue;
        }
        /* SLOT_OCCUPIED */
        if (strcmp(s->key, key) == 0) return pos;
    }
    /* Table is completely full of tombstones — shouldn't happen after resize */
    return tombstone != (size_t)-1 ? tombstone : idx;
}

/* ── resize ───────────────────────────────────────────────────────────────── */

static void ht_resize(HashTable *ht, size_t new_cap) {
    Slot *old_slots = ht->slots;
    size_t old_cap  = ht->capacity;

    ht->slots    = alloc_slots(new_cap);
    ht->capacity = new_cap;
    ht->count    = 0;
    ht->deleted  = 0;

    /* Re-insert all live entries into the new slots array */
    for (size_t i = 0; i < old_cap; i++) {
        if (old_slots[i].state == SLOT_OCCUPIED) {
            size_t pos = probe(ht->slots, new_cap, old_slots[i].key);
            ht->slots[pos].key   = old_slots[i].key;  /* transfer ownership */
            ht->slots[pos].value = old_slots[i].value;
            ht->slots[pos].state = SLOT_OCCUPIED;
            ht->count++;
        } else {
            /* Free key strings of deleted (tombstone) slots */
            free(old_slots[i].key);
        }
    }
    free(old_slots);
}

/* ── lifecycle ────────────────────────────────────────────────────────────── */

HashTable *ht_create(size_t capacity) {
    HashTable *ht = malloc(sizeof(HashTable));
    if (!ht) { perror("malloc HashTable"); exit(EXIT_FAILURE); }

    ht->capacity = next_pow2(capacity, INITIAL_CAPACITY);
    ht->slots    = alloc_slots(ht->capacity);
    ht->count    = 0;
    ht->deleted  = 0;
    return ht;
}

void ht_free(HashTable *ht) {
    if (!ht) return;
    for (size_t i = 0; i < ht->capacity; i++) {
        free(ht->slots[i].key);   /* free() of NULL is a no-op */
    }
    free(ht->slots);
    free(ht);
}

/* ── operations ───────────────────────────────────────────────────────────── */

void ht_set(HashTable *ht, const char *key, int value) {
    if (!ht || !key) return;

    /* Resize before inserting if needed */
    double load = (double)(ht->count + ht->deleted) / (double)ht->capacity;
    if (load >= LOAD_FACTOR_MAX) {
        ht_resize(ht, ht->capacity * 2);
    }

    size_t pos = probe(ht->slots, ht->capacity, key);
    Slot *s    = &ht->slots[pos];

    if (s->state == SLOT_OCCUPIED) {
        /* Update existing key */
        s->value = value;
        return;
    }

    /* New entry — copy the key string */
    if (s->state == SLOT_DELETED) {
        free(s->key);
        ht->deleted--;
    }
    s->key   = strdup(key);
    if (!s->key) { perror("strdup"); exit(EXIT_FAILURE); }
    s->value = value;
    s->state = SLOT_OCCUPIED;
    ht->count++;
}

int ht_get(const HashTable *ht, const char *key, int *value_out) {
    if (!ht || !key) return 0;

    size_t pos = probe(ht->slots, ht->capacity, key);
    const Slot *s = &ht->slots[pos];

    if (s->state == SLOT_OCCUPIED && strcmp(s->key, key) == 0) {
        if (value_out) *value_out = s->value;
        return 1;
    }
    return 0;
}

int ht_delete(HashTable *ht, const char *key) {
    if (!ht || !key) return 0;

    size_t pos = probe(ht->slots, ht->capacity, key);
    Slot *s    = &ht->slots[pos];

    if (s->state != SLOT_OCCUPIED || strcmp(s->key, key) != 0) return 0;

    free(s->key);
    s->key   = NULL;
    s->state = SLOT_DELETED;
    ht->count--;
    ht->deleted++;
    return 1;
}

/* ── inspection ───────────────────────────────────────────────────────────── */

size_t ht_count(const HashTable *ht) {
    return ht ? ht->count : 0;
}

void ht_print(const HashTable *ht) {
    if (!ht) { printf("  (null)\n"); return; }
    printf("  HashTable — capacity=%zu  count=%zu  deleted=%zu  "
           "load=%.2f\n",
           ht->capacity, ht->count, ht->deleted,
           (double)ht->count / (double)ht->capacity);
    for (size_t i = 0; i < ht->capacity; i++) {
        if (ht->slots[i].state == SLOT_OCCUPIED) {
            printf("    [%3zu]  %-20s  =>  %d\n",
                   i, ht->slots[i].key, ht->slots[i].value);
        }
    }
}

/* ── demo main ────────────────────────────────────────────────────────────── */

static void section(const char *title) { printf("\n===== %s =====\n", title); }

int main(void) {
    printf("==========================================================\n");
    printf("  Hash Table Demo — open addressing, linear probing, djb2\n");
    printf("==========================================================\n");

    HashTable *ht = ht_create(8);

    section("insert 10 entries (should trigger a resize from 16 → 32)");
    const char *words[] = {"apple","banana","cherry","date","elderberry",
                           "fig","grape","honeydew","kiwi","lemon"};
    for (int i = 0; i < 10; i++) {
        ht_set(ht, words[i], i * 7);
        printf("  set %-12s => %d\n", words[i], i * 7);
    }
    ht_print(ht);

    section("get");
    int v = 0;
    printf("  get(\"cherry\") = %s",  ht_get(ht, "cherry", &v)  ? "" : "NOT FOUND");
    if (ht_get(ht, "cherry", &v)) printf("%d\n", v);
    printf("  get(\"durian\") = %s\n", ht_get(ht, "durian", &v)  ? "found" : "NOT FOUND");

    section("update existing key");
    ht_set(ht, "apple", 999);
    ht_get(ht, "apple", &v);
    printf("  apple => %d\n", v);

    section("delete \"banana\" and \"fig\"");
    printf("  delete(banana): %s\n", ht_delete(ht, "banana") ? "ok" : "fail");
    printf("  delete(fig):    %s\n", ht_delete(ht, "fig")    ? "ok" : "fail");
    printf("  delete(fig):    %s (second time)\n", ht_delete(ht, "fig") ? "ok" : "fail");
    ht_print(ht);

    ht_free(ht);
    printf("\nDone.\n");
    return 0;
}
