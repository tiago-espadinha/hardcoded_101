/*
 * hash_table.h — Open-addressing hash table (linear probing).
 *
 * Keys:   null-terminated C strings
 * Values: int
 * Hash:   djb2
 * Resize: doubles capacity when load factor exceeds 0.70
 */

#ifndef HASH_TABLE_H
#define HASH_TABLE_H

#include <stddef.h>  /* size_t */

/* ── types ────────────────────────────────────────────────────────────────── */

typedef enum {
    SLOT_EMPTY,    /* never used */
    SLOT_OCCUPIED,
    SLOT_DELETED   /* tombstone — used by linear probing */
} SlotState;

typedef struct {
    char      *key;   /* heap-allocated copy of the key string */
    int        value;
    SlotState  state;
} Slot;

typedef struct {
    Slot   *slots;
    size_t  capacity;  /* total bucket count — always a power of two */
    size_t  count;     /* SLOT_OCCUPIED entries */
    size_t  deleted;   /* SLOT_DELETED tombstones */
} HashTable;

/* ── lifecycle ────────────────────────────────────────────────────────────── */

/* Allocate and initialise a hash table with the given initial capacity.
 * capacity is rounded up to the next power of two (minimum 16). */
HashTable *ht_create(size_t capacity);

/* Free all memory owned by the table (keys + slots array + struct itself). */
void ht_free(HashTable *ht);

/* ── operations ───────────────────────────────────────────────────────────── */

/* O(1) amortised — insert or update key→value. */
void ht_set(HashTable *ht, const char *key, int value);

/*
 * O(1) amortised — look up key.
 * Returns 1 and writes *value_out on success; returns 0 if not found.
 */
int ht_get(const HashTable *ht, const char *key, int *value_out);

/*
 * O(1) amortised — remove key from the table.
 * Returns 1 if removed, 0 if not found.
 */
int ht_delete(HashTable *ht, const char *key);

/* ── inspection ───────────────────────────────────────────────────────────── */

/* Number of live entries. */
size_t ht_count(const HashTable *ht);

/* Print all occupied slots with their bucket index and load factor. */
void ht_print(const HashTable *ht);

#endif /* HASH_TABLE_H */
