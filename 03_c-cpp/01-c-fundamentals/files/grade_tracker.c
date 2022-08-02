/*
 * grade_tracker.c — Command-line grade tracker backed by a CSV file.
 *
 * Usage:
 *   ./grade_tracker add <name> <g1> <g2> <g3>
 *   ./grade_tracker list
 *   ./grade_tracker average <id>
 *   ./grade_tracker top <N>
 *
 * CSV format: id,name,grade1,grade2,grade3
 *
 * Compile:
 *   gcc -std=c17 -Wall -Wextra -Werror -fsanitize=address,undefined \
 *       -o grade_tracker grade_tracker.c
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* ── constants ────────────────────────────────────────────────────────────── */

#define CSV_FILE    "students.csv"
#define NAME_MAX    64
#define GRADES_N    3
#define STUDENTS_MAX 256

/* ── types ────────────────────────────────────────────────────────────────── */

typedef struct {
    int   id;
    char  name[NAME_MAX];
    float grades[GRADES_N];
} Student;

/* ── in-memory store ──────────────────────────────────────────────────────── */

static Student db[STUDENTS_MAX];
static int     db_count = 0;

/* ── CSV I/O ──────────────────────────────────────────────────────────────── */

static void csv_load(void) {
    FILE *f = fopen(CSV_FILE, "r");
    if (!f) return;   /* first run — no file yet */

    char line[256];
    while (fgets(line, sizeof(line), f) && db_count < STUDENTS_MAX) {
        Student *s = &db[db_count];
        int n = sscanf(line, "%d,%63[^,],%f,%f,%f",
                       &s->id, s->name,
                       &s->grades[0], &s->grades[1], &s->grades[2]);
        if (n == 5) db_count++;
    }
    fclose(f);
}

static void csv_save(void) {
    FILE *f = fopen(CSV_FILE, "w");
    if (!f) { perror("fopen"); return; }

    for (int i = 0; i < db_count; i++) {
        fprintf(f, "%d,%s,%.2f,%.2f,%.2f\n",
                db[i].id, db[i].name,
                db[i].grades[0], db[i].grades[1], db[i].grades[2]);
    }
    fclose(f);
}

/* ── helpers ──────────────────────────────────────────────────────────────── */

static int next_id(void) {
    int max = 0;
    for (int i = 0; i < db_count; i++)
        if (db[i].id > max) max = db[i].id;
    return max + 1;
}

static float average(const Student *s) {
    float sum = 0.0f;
    for (int i = 0; i < GRADES_N; i++) sum += s->grades[i];
    return sum / GRADES_N;
}

static void print_header(void) {
    printf("  %-4s  %-20s  %-7s  %-7s  %-7s  %-7s\n",
           "ID", "Name", "G1", "G2", "G3", "Avg");
    printf("  %-4s  %-20s  %-7s  %-7s  %-7s  %-7s\n",
           "----", "--------------------", "-------", "-------", "-------", "-------");
}

static void print_row(const Student *s) {
    printf("  %-4d  %-20s  %-7.2f  %-7.2f  %-7.2f  %-7.2f\n",
           s->id, s->name,
           s->grades[0], s->grades[1], s->grades[2],
           average(s));
}

/* ── commands ─────────────────────────────────────────────────────────────── */

static int cmd_add(const char *name, float g1, float g2, float g3) {
    if (db_count >= STUDENTS_MAX) {
        fprintf(stderr, "Error: database full.\n");
        return 1;
    }
    Student *s = &db[db_count++];
    s->id        = next_id();
    strncpy(s->name, name, NAME_MAX - 1);
    s->name[NAME_MAX - 1] = '\0';
    s->grades[0] = g1;
    s->grades[1] = g2;
    s->grades[2] = g3;
    printf("  Added: [%d] %s  (%.2f, %.2f, %.2f)\n",
           s->id, s->name, g1, g2, g3);
    return 0;
}

static void cmd_list(void) {
    if (db_count == 0) { printf("  No students on record.\n"); return; }
    print_header();
    for (int i = 0; i < db_count; i++) print_row(&db[i]);
    printf("  (%d student%s)\n", db_count, db_count == 1 ? "" : "s");
}

static void cmd_average(int id) {
    for (int i = 0; i < db_count; i++) {
        if (db[i].id == id) {
            printf("  Average for [%d] %s: %.2f\n",
                   db[i].id, db[i].name, average(&db[i]));
            return;
        }
    }
    fprintf(stderr, "  Error: no student with ID %d.\n", id);
}

/* Partial insertion sort to find top N by average — O(n*N) */
static void cmd_top(int n) {
    if (n <= 0 || db_count == 0) { printf("  Nothing to show.\n"); return; }
    if (n > db_count) n = db_count;

    /* copy indices and sort descending by average */
    int idx[STUDENTS_MAX];
    for (int i = 0; i < db_count; i++) idx[i] = i;

    for (int i = 0; i < db_count - 1; i++) {
        for (int j = i + 1; j < db_count; j++) {
            if (average(&db[idx[j]]) > average(&db[idx[i]])) {
                int tmp = idx[i]; idx[i] = idx[j]; idx[j] = tmp;
            }
        }
    }

    printf("  Top %d student%s:\n", n, n == 1 ? "" : "s");
    print_header();
    for (int i = 0; i < n; i++) print_row(&db[idx[i]]);
}

/* ── entry point ──────────────────────────────────────────────────────────── */

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr,
            "Usage:\n"
            "  %s add <name> <g1> <g2> <g3>\n"
            "  %s list\n"
            "  %s average <id>\n"
            "  %s top <N>\n",
            argv[0], argv[0], argv[0], argv[0]);
        return 1;
    }

    csv_load();

    int rc = 0;
    const char *cmd = argv[1];

    if (strcmp(cmd, "add") == 0) {
        if (argc != 6) { fprintf(stderr, "Usage: %s add <name> <g1> <g2> <g3>\n", argv[0]); return 1; }
        rc = cmd_add(argv[2], atof(argv[3]), atof(argv[4]), atof(argv[5]));

    } else if (strcmp(cmd, "list") == 0) {
        cmd_list();

    } else if (strcmp(cmd, "average") == 0) {
        if (argc != 3) { fprintf(stderr, "Usage: %s average <id>\n", argv[0]); return 1; }
        cmd_average(atoi(argv[2]));

    } else if (strcmp(cmd, "top") == 0) {
        if (argc != 3) { fprintf(stderr, "Usage: %s top <N>\n", argv[0]); return 1; }
        cmd_top(atoi(argv[2]));

    } else {
        fprintf(stderr, "Unknown command: %s\n", cmd);
        return 1;
    }

    csv_save();
    return rc;
}
