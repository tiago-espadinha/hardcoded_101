/*
 * 04_strings.c — Custom string functions and common string bugs.
 *
 * Implements from scratch (no string.h):
 *   my_strlen, my_strcpy, my_strcat, my_strcmp, my_strrev
 *
 * Demonstrates common bugs:
 *   - Off-by-one in buffer writes
 *   - Missing null terminator
 *   - (Conceptual) buffer overflow — explained but NOT executed unsafely
 *
 * Compile:
 *   gcc -std=c17 -Wall -Wextra -Werror -fsanitize=address,undefined \
 *       -o 04_strings 04_strings.c
 */

#include <stdio.h>
#include <stdlib.h>

/* ── custom string functions ──────────────────────────────────────────────── */

/*
 * my_strlen — count bytes up to (not including) the null terminator.
 *
 * @param s  null-terminated string
 * @returns  number of characters (excluding '\0')
 * Time: O(n)
 */
static size_t my_strlen(const char *s) {
    const char *p = s;
    while (*p != '\0') p++;
    return (size_t)(p - s);
}

/*
 * my_strcpy — copy src (including '\0') into dst.
 *             dst must have room for my_strlen(src)+1 bytes.
 *
 * @param dst  destination buffer (must be large enough)
 * @param src  null-terminated source string
 * @returns    dst
 * Time: O(n)
 */
static char *my_strcpy(char *dst, const char *src) {
    char *out = dst;
    while ((*dst++ = *src++) != '\0')
        ;   /* loop body is the assignment */
    return out;
}

/*
 * my_strcat — append src to the end of dst.
 *             dst must have room for strlen(dst)+strlen(src)+1 bytes.
 *
 * @param dst  destination (null-terminated, with extra space)
 * @param src  string to append
 * @returns    dst
 * Time: O(n + m) where n = len(dst), m = len(src)
 */
static char *my_strcat(char *dst, const char *src) {
    char *end = dst;
    while (*end != '\0') end++;   /* walk to terminator */
    while ((*end++ = *src++) != '\0')
        ;
    return dst;
}

/*
 * my_strcmp — lexicographic comparison of two strings.
 *
 * @param a  first string
 * @param b  second string
 * @returns  <0 if a<b, 0 if a==b, >0 if a>b
 * Time: O(n)
 */
static int my_strcmp(const char *a, const char *b) {
    while (*a != '\0' && *a == *b) {
        a++;
        b++;
    }
    return (unsigned char)*a - (unsigned char)*b;
}

/*
 * my_strrev — reverse a string in-place.
 *
 * @param s  null-terminated string to reverse
 * Time: O(n)
 */
static void my_strrev(char *s) {
    char *lo = s;
    char *hi = s + my_strlen(s) - 1;
    while (lo < hi) {
        char tmp = *lo;
        *lo++ = *hi;
        *hi-- = tmp;
    }
}

/* ── demonstrations ───────────────────────────────────────────────────────── */

static void print_separator(const char *title) {
    printf("\n===== %s =====\n", title);
}

static void demo_strlen(void) {
    print_separator("my_strlen");
    const char *tests[] = { "hello", "", "C", "null terminator\0invisible", NULL };
    size_t      expected[] = { 5, 0, 1, 15 };

    for (int i = 0; tests[i] != NULL; i++) {
        size_t got = my_strlen(tests[i]);
        printf("  my_strlen(\"%s\") = %zu  %s\n",
               tests[i], got,
               got == expected[i] ? "OK" : "FAIL");
    }
}

static void demo_strcpy(void) {
    print_separator("my_strcpy");

    char buf[32];
    my_strcpy(buf, "Hello, C!");
    printf("  Copied: \"%s\"\n", buf);

    /* show the null byte is at the right place */
    printf("  buf[9] = '\\%d' (should be 0 = null terminator)\n", (int)buf[9]);
}

static void demo_strcat(void) {
    print_separator("my_strcat");

    char buf[64];
    my_strcpy(buf, "foo");
    my_strcat(buf, "bar");
    my_strcat(buf, "baz");
    printf("  \"foo\" + \"bar\" + \"baz\" = \"%s\"\n", buf);
}

static void demo_strcmp(void) {
    print_separator("my_strcmp");

    struct { const char *a; const char *b; } pairs[] = {
        {"apple", "apple"},
        {"apple", "banana"},
        {"banana", "apple"},
        {"", ""},
        {"a", ""},
    };

    for (size_t i = 0; i < sizeof(pairs)/sizeof(pairs[0]); i++) {
        int r = my_strcmp(pairs[i].a, pairs[i].b);
        const char *rel = r < 0 ? "<" : r > 0 ? ">" : "==";
        printf("  \"%s\" %s \"%s\"  (returned %d)\n",
               pairs[i].a, rel, pairs[i].b, r);
    }
}

static void demo_strrev(void) {
    print_separator("my_strrev");

    const char *originals[] = {"hello", "abcde", "a", "", "racecar"};

    for (size_t i = 0; i < sizeof(originals)/sizeof(originals[0]); i++) {
        /* copy to a mutable buffer */
        char buf[64];
        my_strcpy(buf, originals[i]);
        my_strrev(buf);
        printf("  reverse(\"%s\") = \"%s\"\n", originals[i], buf);
    }
}

static void demo_common_bugs(void) {
    print_separator("Common Bugs — Explained");

    /* ── Bug 1: off-by-one ──────────────────────────────────────────────── */
    printf("\n  Bug 1: Off-by-one in manual copy loop\n");
    printf("    BAD pattern:  for (i = 0; i < len; i++) dst[i] = src[i];\n");
    printf("    This copies len bytes but forgets the null terminator at dst[len].\n");
    printf("    FIX: copy len+1 bytes, or use my_strcpy which copies until '\\0'.\n");

    /* Safe demonstration: we fix it */
    const char *src = "oops";
    size_t len = my_strlen(src);
    char *fixed = malloc(len + 1);
    if (fixed) {
        for (size_t i = 0; i <= len; i++) fixed[i] = src[i];  /* <= includes '\0' */
        printf("    Fixed copy: \"%s\" (null at index %zu)\n", fixed, len);
        free(fixed);
    }

    /* ── Bug 2: buffer overflow (conceptual) ─────────────────────────────── */
    printf("\n  Bug 2: Buffer overflow\n");
    printf("    char buf[5];\n");
    printf("    my_strcpy(buf, \"hello world\");  // writes 12 bytes into 5-byte buf!\n");
    printf("    With -fsanitize=address this aborts immediately:\n");
    printf("      ERROR: AddressSanitizer: stack-buffer-overflow\n");
    printf("    FIX: always check length before copying, or use safe variants.\n");

    /* ── Bug 3: missing null terminator ─────────────────────────────────── */
    printf("\n  Bug 3: Missing null terminator\n");
    printf("    char buf[3] = {'a', 'b', 'c'};  // no '\\0'!\n");
    printf("    printf(\"%%s\", buf);  // reads past buf until it stumbles on a 0 byte\n");
    printf("    FIX: char buf[4] = {'a', 'b', 'c', '\\0'}; or char buf[] = \"abc\";\n");
}

/* ── entry point ──────────────────────────────────────────────────────────── */

int main(void) {
    printf("==========================================================\n");
    printf("  04_strings — Custom String Functions in C\n");
    printf("==========================================================\n");

    demo_strlen();
    demo_strcpy();
    demo_strcat();
    demo_strcmp();
    demo_strrev();
    demo_common_bugs();

    printf("\nDone.\n");
    return 0;
}
