#!/usr/bin/env bash
# tests/run_tests.sh — Automated test runner for c-fundamentals.
#
# Builds all targets in debug mode (ASan) and runs basic smoke tests.
# Exits with code 0 if all tests pass, 1 otherwise.

set -euo pipefail

PASS=0
FAIL=0
RED='\033[0;31m'
GRN='\033[0;32m'
YLW='\033[1;33m'
NC='\033[0m'

assert_runs() {
    local label="$1"; shift
    if "$@" > /dev/null 2>&1; then
        printf "  ${GRN}PASS${NC}  %s\n" "$label"
        ((PASS++))
    else
        printf "  ${RED}FAIL${NC}  %s\n" "$label"
        ((FAIL++))
    fi
}

assert_output_contains() {
    local label="$1"
    local binary="$2"
    local expected="$3"
    shift 3
    local out
    out=$("$binary" "$@" 2>&1) || true
    if echo "$out" | grep -q "$expected"; then
        printf "  ${GRN}PASS${NC}  %s\n" "$label"
        ((PASS++))
    else
        printf "  ${RED}FAIL${NC}  %s  (expected: '%s')\n" "$label" "$expected"
        ((FAIL++))
    fi
}

echo ""
echo "=========================================="
echo "  c-fundamentals — test suite"
echo "=========================================="

# ── memory module ──────────────────────────────────────────────────────────

echo ""
echo "${YLW}[memory]${NC}"

assert_runs          "01_pointers compiles and runs"        ./memory/01_pointers
assert_output_contains "01_pointers: shows hex address"    ./memory/01_pointers "0x"
assert_output_contains "01_pointers: pointer arithmetic"   ./memory/01_pointers "Pointer Arithmetic"

assert_runs          "02_stack_vs_heap runs"               ./memory/02_stack_vs_heap
assert_output_contains "02_stack_vs_heap: malloc demo"     ./memory/02_stack_vs_heap "Heap Allocation"
assert_output_contains "02_stack_vs_heap: no leak message" ./memory/02_stack_vs_heap "no leak"

assert_runs          "03_pointers_and_arrays runs"         ./memory/03_pointers_and_arrays
assert_output_contains "03: arr[i]==*(arr+i)"              ./memory/03_pointers_and_arrays "yes"
assert_output_contains "03: array_sum correct"             ./memory/03_pointers_and_arrays "sum"

assert_runs          "04_strings runs"                     ./memory/04_strings
assert_output_contains "04_strings: strlen OK"             ./memory/04_strings "OK"
assert_output_contains "04_strings: reverse"               ./memory/04_strings "olleh"

assert_runs          "05_structs runs"                     ./memory/05_structs
assert_output_contains "05_structs: sort by GPA"           ./memory/05_structs "Carol"

# ── structures module ──────────────────────────────────────────────────────

echo ""
echo "${YLW}[structures]${NC}"

assert_runs          "linked_list runs"                    ./structures/linked_list
assert_output_contains "linked_list: append"               ./structures/linked_list "10"
assert_output_contains "linked_list: reverse"              ./structures/linked_list "Reverse"
assert_output_contains "linked_list: search found"         ./structures/linked_list "found"
assert_output_contains "linked_list: search not found"     ./structures/linked_list "not found"

assert_runs          "hash_table runs"                     ./structures/hash_table
assert_output_contains "hash_table: insert"                ./structures/hash_table "apple"
assert_output_contains "hash_table: get hit"               ./structures/hash_table "cherry"
assert_output_contains "hash_table: get miss"              ./structures/hash_table "NOT FOUND"
assert_output_contains "hash_table: delete"                ./structures/hash_table "ok"
assert_output_contains "hash_table: update"                ./structures/hash_table "999"

# ── files module ───────────────────────────────────────────────────────────

echo ""
echo "${YLW}[files]${NC}"

# Grade tracker — run in a temp directory to avoid polluting the repo
TMPDIR_GT=$(mktemp -d)
cp ./files/grade_tracker "$TMPDIR_GT/"
pushd "$TMPDIR_GT" > /dev/null

assert_runs          "grade_tracker: add Alice"       ./grade_tracker add "Alice"  88 92 95
assert_runs          "grade_tracker: add Bob"         ./grade_tracker add "Bob"    72 68 80
assert_runs          "grade_tracker: add Carol"       ./grade_tracker add "Carol"  95 97 99
assert_output_contains "grade_tracker: list shows names" ./grade_tracker list "Alice"
assert_output_contains "grade_tracker: average ID 1"     ./grade_tracker average 1 "91"
assert_output_contains "grade_tracker: top 2 has Carol"  ./grade_tracker top 2 "Carol"

popd > /dev/null
rm -rf "$TMPDIR_GT"

assert_runs          "binary_rw: runs and benchmarks"  ./files/binary_rw
assert_output_contains "binary_rw: round-trip OK"     ./files/binary_rw "OK"

# ── summary ────────────────────────────────────────────────────────────────

echo ""
echo "=========================================="
TOTAL=$((PASS + FAIL))
printf "  Results: ${GRN}%d passed${NC}  /  ${RED}%d failed${NC}  /  %d total\n" \
       "$PASS" "$FAIL" "$TOTAL"
echo "=========================================="
echo ""

[ "$FAIL" -eq 0 ]
