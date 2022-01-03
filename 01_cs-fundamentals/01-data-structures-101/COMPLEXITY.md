# Data Structure Complexities

| Structure          | Access   | Search   | Insert   | Delete   | Space |
|--------------------|----------|----------|----------|----------|-------|
| Singly Linked List | O(n)     | O(n)     | O(1)*    | O(n)     | O(n)  |
| Doubly Linked List | O(n)     | O(n)     | O(1)*    | O(1)**   | O(n)  |
| Stack              | O(n)     | O(n)     | O(1)     | O(1)     | O(n)  |
| Queue              | O(n)     | O(n)     | O(1)     | O(1)     | O(n)  |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | O(log n) | O(n)  |
| Hash Map           | N/A      | O(1)***  | O(1)***  | O(1)***  | O(n)  |

\* O(1) for prepend/append if tail is tracked.

\** O(1) if node is already known.

\*** Average case. Worst case is O(n).
