/*
 * 05_structs.c — Structs, pass-by-value vs pass-by-pointer, insertion sort.
 *
 * Compile:
 *   gcc -std=c17 -Wall -Wextra -Werror -fsanitize=address,undefined \
 *       -o 05_structs 05_structs.c
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* ── type definitions ─────────────────────────────────────────────────────── */

#define NAME_MAX 50
#define NUM_STUDENTS 5

typedef struct {
    char  name[NAME_MAX];
    int   id;
    float gpa;
} Student;

/* ── print helpers ────────────────────────────────────────────────────────── */

static void print_separator(const char *title) {
    printf("\n===== %s =====\n", title);
}

/*
 * print_student — display a single student record.
 *
 * @param s  const pointer — we promise not to modify the student
 * Time: O(1)
 */
static void print_student(const Student *s) {
    printf("  [%03d]  %-20s  GPA: %.2f\n", s->id, s->name, s->gpa);
}

static void print_table(const Student *arr, int n) {
    printf("  %-5s  %-20s  %s\n", "ID", "Name", "GPA");
    printf("  %-5s  %-20s  %s\n", "---", "----", "---");
    for (int i = 0; i < n; i++) print_student(&arr[i]);
}

/* ── pass-by-value vs pass-by-pointer ────────────────────────────────────── */

/*
 * try_bump_gpa_by_value — receives a COPY; changes are invisible to caller.
 * Time: O(1) — but copies the whole struct (50+4+4 = 58 bytes)
 */
static void try_bump_gpa_by_value(Student s, float delta) {
    s.gpa += delta;
    printf("  Inside by-value:   %s GPA = %.2f  (local copy only)\n",
           s.name, s.gpa);
}

/*
 * bump_gpa_by_pointer — receives a pointer; modifies the original.
 * Time: O(1) — only 8 bytes (pointer) copied
 */
static void bump_gpa_by_pointer(Student *s, float delta) {
    s->gpa += delta;
    printf("  Inside by-pointer: %s GPA = %.2f  (original modified)\n",
           s->name, s->gpa);
}

static void demo_pass_semantics(void) {
    print_separator("Pass-by-Value vs Pass-by-Pointer");

    Student alice = {"Alice", 1001, 3.50f};
    printf("  Before: ");
    print_student(&alice);

    try_bump_gpa_by_value(alice, 0.20f);
    printf("  After by-value:   ");
    print_student(&alice);   /* unchanged */

    bump_gpa_by_pointer(&alice, 0.20f);
    printf("  After by-pointer: ");
    print_student(&alice);   /* now 3.70 */
}

/* ── heap allocation of student array ────────────────────────────────────── */

static Student *make_students(void) {
    Student *arr = malloc(NUM_STUDENTS * sizeof(Student));
    if (!arr) { perror("malloc"); exit(EXIT_FAILURE); }

    /* initialise with sample data */
    const char *names[] = {"Alice", "Bob", "Carol", "Dave", "Eve"};
    float gpas[]        = {3.50f, 2.80f, 3.95f, 3.10f, 2.60f};

    for (int i = 0; i < NUM_STUDENTS; i++) {
        strncpy(arr[i].name, names[i], NAME_MAX - 1);
        arr[i].name[NAME_MAX - 1] = '\0';
        arr[i].id  = 1001 + i;
        arr[i].gpa = gpas[i];
    }
    return arr;
}

/* ── insertion sort by GPA (descending) ──────────────────────────────────── */

/*
 * sort_by_gpa — sort students in-place by GPA, highest first.
 *
 * @param students  array of Student
 * @param n         number of elements
 * Time:  O(n²) worst case; O(n) best case (already sorted)
 * Space: O(1) auxiliary
 */
static void sort_by_gpa(Student *students, int n) {
    for (int i = 1; i < n; i++) {
        Student key = students[i];
        int j = i - 1;
        /* shift elements with lower GPA one position right */
        while (j >= 0 && students[j].gpa < key.gpa) {
            students[j + 1] = students[j];
            j--;
        }
        students[j + 1] = key;
    }
}

static void demo_sort(void) {
    print_separator("sort_by_gpa — Insertion Sort");

    Student *arr = make_students();

    printf("  Before sorting:\n");
    print_table(arr, NUM_STUDENTS);

    sort_by_gpa(arr, NUM_STUDENTS);

    printf("\n  After sorting by GPA (descending):\n");
    print_table(arr, NUM_STUDENTS);

    free(arr);
}

/* ── struct size and padding ──────────────────────────────────────────────── */

static void demo_sizeof_struct(void) {
    print_separator("sizeof — Struct Size and Padding");

    printf("  sizeof(Student)        = %zu bytes\n", sizeof(Student));
    printf("  sizeof(char[%d])       = %zu bytes  (name field)\n",
           NAME_MAX, sizeof(((Student*)0)->name));
    printf("  sizeof(int)            = %zu bytes  (id field)\n",    sizeof(int));
    printf("  sizeof(float)          = %zu bytes  (gpa field)\n",   sizeof(float));

    /* The compiler may add padding for alignment */
    size_t manual = NAME_MAX + sizeof(int) + sizeof(float);
    size_t actual = sizeof(Student);
    printf("\n  Manual sum of fields   = %zu bytes\n", manual);
    printf("  Actual sizeof(Student) = %zu bytes\n", actual);
    if (actual > manual)
        printf("  => Compiler added %zu byte(s) of padding for alignment.\n",
               actual - manual);
    else
        printf("  => No padding needed for this layout.\n");
}

/* ── nested structs ───────────────────────────────────────────────────────── */

typedef struct {
    int year;
    int month;
    int day;
} Date;

typedef struct {
    Student  student;
    Date     enrolled;
} Enrollment;

static void demo_nested(void) {
    print_separator("Nested Structs");

    Enrollment e = {
        .student  = {"Zara", 1010, 3.85f},
        .enrolled = {2022, 9, 1},
    };

    printf("  Student: %s (ID %d, GPA %.2f)\n",
           e.student.name, e.student.id, e.student.gpa);
    printf("  Enrolled: %04d-%02d-%02d\n",
           e.enrolled.year, e.enrolled.month, e.enrolled.day);
}

/* ── entry point ──────────────────────────────────────────────────────────── */

int main(void) {
    printf("==========================================================\n");
    printf("  05_structs — Structs in C\n");
    printf("==========================================================\n");

    demo_pass_semantics();
    demo_sort();
    demo_sizeof_struct();
    demo_nested();

    printf("\nDone.\n");
    return 0;
}
