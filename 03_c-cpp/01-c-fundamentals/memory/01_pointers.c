/*
 * 01_pointers.c — Pointer basics, address printing, and pointer arithmetic
 *
 * Compile: gcc -std=c17 -Wall -Wextra -Werror -fsanitize=address,undefined \
 *               -o 01_pointers 01_pointers.c
 */

#include <stdio.h>
#include <stddef.h>  /* ptrdiff_t */

/* ── helpers ──────────────────────────────────────────────────────────────── */

static void print_separator(const char *title) {
    printf("\n===== %s =====\n", title);
}

/* ── demonstrations ───────────────────────────────────────────────────────── */

static void demo_basic_addresses(void) {
    print_separator("Basic Addresses");

    int   i  = 42;
    double d = 3.14;
    char   c = 'A';

    /* & gives the address; %p prints it as hex */
    printf("  int    i  = %d   stored at %p\n", i,  (void *)&i);
    printf("  double d  = %.2f stored at %p\n", d,  (void *)&d);
    printf("  char   c  = '%c' stored at %p\n", c,  (void *)&c);

    /* Sizes — why they differ: type width vs pointer width */
    printf("\n  sizeof(int)    = %zu bytes\n", sizeof(int));
    printf("  sizeof(double) = %zu bytes\n", sizeof(double));
    printf("  sizeof(char)   = %zu bytes\n", sizeof(char));
    printf("  sizeof(int *)  = %zu bytes  (pointer size, platform dependent)\n",
           sizeof(int *));
    printf("  sizeof(double*)= %zu bytes\n", sizeof(double *));
    printf("  sizeof(char *) = %zu bytes\n", sizeof(char *));
}

static void demo_dereference(void) {
    print_separator("Dereference");

    int value = 100;
    int *ptr  = &value;   /* ptr holds the ADDRESS of value */

    printf("  value         = %d\n", value);
    printf("  ptr           = %p  (the address)\n", (void *)ptr);
    printf("  *ptr          = %d  (dereference — reads through the pointer)\n", *ptr);

    *ptr = 200;           /* write through the pointer */
    printf("  After *ptr = 200:  value = %d\n", value);
}

static void demo_pointer_arithmetic(void) {
    print_separator("Pointer Arithmetic on Arrays");

    int arr[5] = {10, 20, 30, 40, 50};
    int *p = arr;   /* arr decays to &arr[0] */

    printf("  arr sits at address: %p\n", (void *)arr);

    for (int i = 0; i < 5; i++) {
        /* p + i advances by i * sizeof(int) bytes */
        printf("  arr[%d] = %d   &arr[%d] = %p   (p+%d) = %p   *(p+%d) = %d\n",
               i, arr[i],
               i, (void *)&arr[i],
               i, (void *)(p + i),
               i, *(p + i));
    }

    /* Pointer subtraction gives element distance, not byte distance */
    int *first = &arr[0];
    int *last  = &arr[4];
    ptrdiff_t dist = last - first;
    printf("\n  last - first  = %td elements  (%td bytes)\n",
           dist, (last - first) * (ptrdiff_t)sizeof(int));
}

static void demo_pointer_to_pointer(void) {
    print_separator("Pointer-to-Pointer");

    int  x   = 7;
    int *p   = &x;
    int **pp = &p;   /* pointer to a pointer */

    printf("  x    = %d   at %p\n", x, (void *)&x);
    printf("  p    = %p   at %p\n", (void *)p, (void *)&p);
    printf("  pp   = %p   at %p\n", (void *)pp, (void *)&pp);
    printf("  *p   = %d\n", *p);
    printf("  **pp = %d\n", **pp);

    **pp = 99;
    printf("  After **pp = 99:  x = %d\n", x);
}

/* ── entry point ──────────────────────────────────────────────────────────── */

int main(void) {
    printf("==========================================================\n");
    printf("  01_pointers — Pointer Fundamentals in C\n");
    printf("==========================================================\n");

    demo_basic_addresses();
    demo_dereference();
    demo_pointer_arithmetic();
    demo_pointer_to_pointer();

    printf("\nDone.\n");
    return 0;
}
