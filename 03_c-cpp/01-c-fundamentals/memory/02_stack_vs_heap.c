/*
 * 02_stack_vs_heap.c — Stack allocation vs heap allocation, leak demo, ASan
 *
 * Compile (debug — ASan catches issues at runtime):
 *   gcc -std=c17 -Wall -Wextra -Werror -g \
 *       -fsanitize=address,undefined \
 *       -o 02_stack_vs_heap 02_stack_vs_heap.c
 *
 * Compile (release — no sanitizers):
 *   gcc -std=c17 -Wall -Wextra -O2 -o 02_stack_vs_heap 02_stack_vs_heap.c
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ARRAY_SIZE 8

/* ── helpers ──────────────────────────────────────────────────────────────── */

static void print_separator(const char *title) {
    printf("\n===== %s =====\n", title);
}

static void print_array(const char *label, const int *arr, size_t n) {
    printf("  %s: [", label);
    for (size_t i = 0; i < n; i++) {
        printf("%d%s", arr[i], i + 1 < n ? ", " : "");
    }
    printf("]\n");
}

/* ── stack allocation ─────────────────────────────────────────────────────── */

static void demo_stack(void) {
    print_separator("Stack Allocation");

    /*
     * Stack arrays are allocated automatically when the function is called
     * and freed automatically when it returns. No malloc/free needed.
     * Size must be known at compile time (or use a VLA — avoid in practice).
     */
    int stack_arr[ARRAY_SIZE];

    for (int i = 0; i < ARRAY_SIZE; i++) {
        stack_arr[i] = (i + 1) * 10;
    }

    printf("  Stack array lives at: %p\n", (void *)stack_arr);
    print_array("stack_arr", stack_arr, ARRAY_SIZE);
    printf("  sizeof(stack_arr) = %zu bytes (%d ints × %zu)\n",
           sizeof(stack_arr), ARRAY_SIZE, sizeof(int));
    printf("  NOTE: stack memory is automatically reclaimed when this\n");
    printf("        function returns — no cleanup needed.\n");
}

/* ── heap allocation ──────────────────────────────────────────────────────── */

static void demo_heap(void) {
    print_separator("Heap Allocation (malloc / free)");

    /*
     * Heap allocation lets you decide size at runtime and keep the memory
     * alive beyond the function that allocated it. YOU are responsible for
     * calling free() exactly once when done.
     */
    size_t n = ARRAY_SIZE;
    int *heap_arr = malloc(n * sizeof(int));

    if (heap_arr == NULL) {
        fprintf(stderr, "  malloc failed!\n");
        return;
    }

    for (size_t i = 0; i < n; i++) {
        heap_arr[i] = (int)(i + 1) * 100;
    }

    printf("  Heap array lives at:  %p\n", (void *)heap_arr);
    print_array("heap_arr", heap_arr, n);
    printf("  This pointer can outlive this function — callers can use it.\n");

    free(heap_arr);  /* <-- mandatory; omitting this is a memory leak */
    heap_arr = NULL; /* defensive: prevents accidental use-after-free */
    printf("  free() called — memory returned to allocator.\n");
}

/* ── calloc vs malloc ─────────────────────────────────────────────────────── */

static void demo_calloc(void) {
    print_separator("calloc — zero-initialised heap memory");

    int *arr = calloc(ARRAY_SIZE, sizeof(int));  /* fills with 0s */
    if (!arr) { perror("calloc"); return; }

    printf("  calloc gives zeroed memory:\n");
    print_array("arr (before write)", arr, ARRAY_SIZE);

    for (int i = 0; i < ARRAY_SIZE; i++) arr[i] = i * i;
    print_array("arr (after write) ", arr, ARRAY_SIZE);

    free(arr);
}

/* ── realloc ──────────────────────────────────────────────────────────────── */

static void demo_realloc(void) {
    print_separator("realloc — grow a heap buffer");

    int *arr = malloc(4 * sizeof(int));
    if (!arr) { perror("malloc"); return; }

    for (int i = 0; i < 4; i++) arr[i] = i + 1;
    printf("  Before realloc (4 ints): ");
    print_array("arr", arr, 4);

    int *bigger = realloc(arr, 8 * sizeof(int));
    if (!bigger) { perror("realloc"); free(arr); return; }
    arr = bigger;  /* arr may have moved; NEVER use old pointer after realloc */

    for (int i = 4; i < 8; i++) arr[i] = i + 1;
    printf("  After realloc  (8 ints): ");
    print_array("arr", arr, 8);

    free(arr);
}

/* ── dangling pointer (UB — commented out, explained in text) ────────────── */

/*
 * DANGER ZONE — do NOT uncomment; this demonstrates undefined behaviour.
 *
 * static int *returns_stack_address(void) {
 *     int local = 42;
 *     return &local;   // BAD: 'local' ceases to exist when function returns
 * }
 *
 * In main():
 *     int *p = returns_stack_address();
 *     printf("%d\n", *p);   // UB — stack frame is gone; ASan will abort here
 *
 * With -fsanitize=address you get:
 *   ERROR: AddressSanitizer: stack-use-after-return
 */

/* ── simulated leak (safe: we show what ASan reports, then fix it) ────────── */

static void demo_leak_then_fix(void) {
    print_separator("Memory Leak Detection");

    printf("  Allocating 1 KB on the heap...\n");
    char *buf = malloc(1024);
    if (!buf) { perror("malloc"); return; }

    strncpy(buf, "This buffer must be freed", 1023);
    buf[1023] = '\0';
    printf("  buf = \"%s\"\n", buf);

    /*
     * If we returned here without calling free(buf), ASan would report:
     *
     *   Direct leak of 1024 byte(s) in 1 object(s) allocated from:
     *       #0 0x... in malloc
     *       #1 0x... in demo_leak_then_fix
     *
     * We always free — this is the CORRECT pattern.
     */
    free(buf);
    printf("  free() called — no leak reported by ASan.\n");
}

/* ── entry point ──────────────────────────────────────────────────────────── */

int main(void) {
    printf("==========================================================\n");
    printf("  02_stack_vs_heap — Memory Allocation in C\n");
    printf("==========================================================\n");

    demo_stack();
    demo_heap();
    demo_calloc();
    demo_realloc();
    demo_leak_then_fix();

    printf("\nAll demos complete — no leaks if compiled with ASan.\n");
    return 0;
}
