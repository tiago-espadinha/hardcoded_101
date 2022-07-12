/*
 * 03_pointers_and_arrays.c — arr[i] == *(arr+i), pointer-only arithmetic,
 *                             2D arrays on the heap.
 *
 * Compile:
 *   gcc -std=c17 -Wall -Wextra -Werror -fsanitize=address,undefined \
 *       -o 03_pointers_and_arrays 03_pointers_and_arrays.c
 */

#include <stdio.h>
#include <stdlib.h>

/* ── helpers ──────────────────────────────────────────────────────────────── */

static void print_separator(const char *title) {
    printf("\n===== %s =====\n", title);
}

/* ── arr[i] == *(arr+i) ───────────────────────────────────────────────────── */

static void demo_equivalence(void) {
    print_separator("arr[i]  ==  *(arr + i)");

    int arr[6] = {5, 10, 15, 20, 25, 30};

    printf("  %-6s  %-12s  %-12s  %-8s\n",
           "index", "arr[i]", "*(arr+i)", "equal?");
    printf("  %-6s  %-12s  %-12s  %-8s\n",
           "------", "------", "--------", "------");

    for (int i = 0; i < 6; i++) {
        printf("  %-6d  %-12d  %-12d  %-8s\n",
               i, arr[i], *(arr + i),
               arr[i] == *(arr + i) ? "yes" : "NO");
    }

    /* C also allows the exotic: i[arr] — legal but unreadable! */
    printf("\n  Exotic: 2[arr] = %d   (arr[2] = %d) — same thing!\n",
           2[arr], arr[2]);
}

/* ── array_sum using pointer arithmetic only ─────────────────────────────── */

/*
 * array_sum — sum all elements using pointer arithmetic; no [] operator.
 *
 * @param arr  pointer to first element
 * @param n    number of elements
 * @returns    sum of all elements
 * Time: O(n) — one pass through the array.
 */
static long array_sum(const int *arr, size_t n) {
    long total = 0;
    const int *end = arr + n;   /* one past the last element */

    /* advance p from arr to end — never dereference end itself */
    for (const int *p = arr; p < end; p++) {
        total += *p;
    }
    return total;
}

static void demo_array_sum(void) {
    print_separator("array_sum — pointer arithmetic only (no [])");

    int data[] = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
    size_t len = sizeof(data) / sizeof(data[0]);

    printf("  data = {");
    for (size_t i = 0; i < len; i++) {
        printf("%d%s", data[i], i + 1 < len ? ", " : "");
    }
    printf("}\n");
    printf("  sum  = %ld\n", array_sum(data, len));
}

/* ── 2D array on the heap ─────────────────────────────────────────────────── */

/*
 * alloc_2d — allocate an rows × cols integer matrix on the heap.
 * Returns a pointer to an array of row pointers.
 * Caller must call free_2d() when done.
 */
static int **alloc_2d(size_t rows, size_t cols) {
    /* allocate the row-pointer array */
    int **matrix = malloc(rows * sizeof(int *));
    if (!matrix) { perror("malloc rows"); return NULL; }

    /* allocate each row */
    for (size_t r = 0; r < rows; r++) {
        matrix[r] = malloc(cols * sizeof(int));
        if (!matrix[r]) {
            /* clean up already-allocated rows */
            for (size_t k = 0; k < r; k++) free(matrix[k]);
            free(matrix);
            return NULL;
        }
    }
    return matrix;
}

/*
 * free_2d — release a rows × cols matrix allocated by alloc_2d.
 */
static void free_2d(int **matrix, size_t rows) {
    for (size_t r = 0; r < rows; r++) free(matrix[r]);
    free(matrix);
}

static void demo_2d_heap(void) {
    print_separator("2D Array on the Heap");

    const size_t ROWS = 4, COLS = 5;

    int **m = alloc_2d(ROWS, COLS);
    if (!m) return;

    /* Fill with multiplication table */
    for (size_t r = 0; r < ROWS; r++)
        for (size_t c = 0; c < COLS; c++)
            m[r][c] = (int)((r + 1) * (c + 1));

    printf("  %zu×%zu multiplication table:\n\n", ROWS, COLS);
    printf("       ");
    for (size_t c = 0; c < COLS; c++) printf("  [%zu]", c);
    printf("\n");
    for (size_t r = 0; r < ROWS; r++) {
        printf("  [%zu]  ", r);
        for (size_t c = 0; c < COLS; c++) printf("  %3d", m[r][c]);
        printf("\n");
    }

    /* Demonstrate pointer arithmetic across rows */
    printf("\n  Pointer walk — m[r] is a pointer to its row:\n");
    for (size_t r = 0; r < ROWS; r++) {
        printf("    m[%zu] lives at %p, m[%zu][0] = %d\n",
               r, (void *)m[r], r, m[r][0]);
    }

    free_2d(m, ROWS);
    printf("\n  free_2d() called — all %zu row allocations released.\n", ROWS + 1);
}

/* ── pointer comparison ───────────────────────────────────────────────────── */

static void demo_pointer_comparison(void) {
    print_separator("Pointer Comparison");

    int arr[5] = {10, 20, 30, 40, 50};
    int *lo = arr;
    int *hi = arr + 4;

    printf("  lo = %p  (*lo = %d)\n", (void *)lo, *lo);
    printf("  hi = %p  (*hi = %d)\n", (void *)hi, *hi);
    printf("  lo < hi ? %s\n", lo < hi ? "yes" : "no");
    printf("  hi - lo = %td elements\n", hi - lo);

    /* walk from hi down to lo */
    printf("  Reverse walk: ");
    for (int *p = hi; p >= lo; p--) {
        printf("%d%s", *p, p > lo ? " " : "\n");
    }
}

/* ── entry point ──────────────────────────────────────────────────────────── */

int main(void) {
    printf("==========================================================\n");
    printf("  03_pointers_and_arrays — Pointer/Array Duality in C\n");
    printf("==========================================================\n");

    demo_equivalence();
    demo_array_sum();
    demo_2d_heap();
    demo_pointer_comparison();

    printf("\nDone.\n");
    return 0;
}
