# Selection Sort — Complete DSA Notes

---

## 1. Definition

**Selection Sort** is a simple, in-place, comparison-based sorting algorithm. It works by dividing the array into two logical sublists:

- A **sorted sublist** — built incrementally from left to right.
- An **unsorted sublist** — the remaining elements to the right.

On each pass, the algorithm *selects* the minimum element from the unsorted sublist and swaps it into its correct position at the front of the unsorted region.

> **Core idea:** Find the smallest → swap it to the front → shrink the unsorted region → repeat.

---

## 2. Key Properties

| Property         | Value                          |
|------------------|-------------------------------|
| Type             | In-place, comparison sort      |
| Stable           | ❌ No (standard implementation) |
| Adaptive         | ❌ No (always O(n²))            |
| Extra space      | O(1)                           |
| Total swaps      | At most **n − 1**              |
| Total comparisons| n(n−1)/2 — always              |

---

## 3. How It Works (Step-by-Step)

1. **Set the boundary pointer** — Start with `i = 0`. Everything to the left of `i` is already sorted.
2. **Find the minimum** — Scan from index `i` to `n−1`, recording the index of the smallest element.
3. **Swap** — Swap `arr[minIdx]` with `arr[i]`. Element at position `i` is now in its final, sorted position.
4. **Advance** — Increment `i` and repeat steps 2–3 until `i = n−1`.

**Total passes:** n − 1

**Invariant:** After pass *k*, the first *k* elements are sorted and contain the *k* smallest values of the entire array.

---

## 4. Example Walkthrough

**Input:** `[64, 25, 12, 22, 11]`

### Pass 1 — i = 0
```
[64, 25, 12, 22, 11]   Scan right → minimum is 11 at index 4
 ^                     Swap arr[0] ↔ arr[4]
[11, 25, 12, 22, 64]   ✓ 11 is sorted
```

### Pass 2 — i = 1
```
[11, 25, 12, 22, 64]   Scan right → minimum is 12 at index 2
     ^                 Swap arr[1] ↔ arr[2]
[11, 12, 25, 22, 64]   ✓ 12 is sorted
```

### Pass 3 — i = 2
```
[11, 12, 25, 22, 64]   Scan right → minimum is 22 at index 3
         ^             Swap arr[2] ↔ arr[3]
[11, 12, 22, 25, 64]   ✓ 22 is sorted
```

### Pass 4 — i = 3
```
[11, 12, 22, 25, 64]   Scan right → minimum is 25 at index 3
             ^         Already in position — no swap needed
[11, 12, 22, 25, 64]   ✓ 25 is sorted
```

**Output:** `[11, 12, 22, 25, 64]` ✅

---

## 5. Implementation

### Python

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Assume i is the minimum
        min_idx = i

        # Find actual minimum in the unsorted region
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap minimum into position i (guard avoids redundant swap)
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Example
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # → [11, 12, 22, 25, 64]
```

### JavaScript

```javascript
function selectionSort(arr) {
    const n = arr.length;

    for (let i = 0; i < n - 1; i++) {
        let minIdx = i;

        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }

        if (minIdx !== i) {
            [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];
        }
    }
    return arr;
}

// Example
console.log(selectionSort([64, 25, 12, 22, 11]));
// → [11, 12, 22, 25, 64]
```

### C

```c
#include <stdio.h>

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;

        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx])
                minIdx = j;
        }

        if (minIdx != i) {
            int temp = arr[i];
            arr[i] = arr[minIdx];
            arr[minIdx] = temp;
        }
    }
}
```

> **Note:** The `if minIdx != i` guard prevents a redundant swap when the minimum is already in position. This matters when swaps are expensive (e.g. large structs, records on disk).

---

## 6. Selection Sort vs Bubble Sort

| Property              | Selection Sort    | Bubble Sort       |
|-----------------------|-------------------|-------------------|
| Time — best case      | O(n²)             | **O(n)**          |
| Time — average case   | O(n²)             | O(n²)             |
| Time — worst case     | O(n²)             | O(n²)             |
| Swaps — worst case    | **O(n)**          | O(n²)             |
| Space                 | O(1)              | O(1)              |
| Stable                | ❌ No              | ✅ Yes             |
| Adaptive              | ❌ No              | ✅ Yes             |

**Key insight:** Selection sort makes at most *n−1* swaps, regardless of input order. Bubble sort can make up to n(n−1)/2 swaps in the worst case. This makes selection sort preferable when **memory writes are significantly more costly than reads** (e.g. flash memory, EEPROM).

Bubble sort has an advantage when the input is **nearly sorted** — it can detect this early and exit in O(n). Selection sort cannot.

---

## 7. Complexity Analysis

### Time Complexity

The outer loop runs **n−1** times. The inner loop scans:

```
Pass 0: n−1 comparisons
Pass 1: n−2 comparisons
...
Pass n−2: 1 comparison

Total = (n−1) + (n−2) + ... + 1 = n(n−1)/2
```

This is **Θ(n²)** in all cases — there is no early termination. Selection sort cannot detect a sorted array without completing every scan.

| Case    | Time Complexity |
|---------|----------------|
| Best    | O(n²)          |
| Average | O(n²)          |
| Worst   | O(n²)          |

### Space Complexity

**O(1)** — in-place algorithm. Only a few integer variables (`i`, `j`, `minIdx`, `temp`) are used, regardless of input size.

### Swap Count

| n      | Comparisons   | Max swaps |
|--------|---------------|-----------|
| 10     | 45            | 9         |
| 100    | 4,950         | 99        |
| 1,000  | 499,500       | 999       |
| 10,000 | 49,995,000    | 9,999     |

---

## 8. Stability

Selection sort is **not stable** in its standard form. Equal elements may be reordered during swaps.

**Example:**
```
Input:  [(3, a), (3, b), (1, c)]
After selection sort:  [(1, c), (3, b), (3, a)]
```
The two elements with key `3` have swapped relative order. A stable sort would preserve `(3, a)` before `(3, b)`.

> Selection sort can be made stable by using **insertion** instead of swapping (shifting elements rather than jumping past them), but this changes the time constant and defeats part of the purpose.

---

## 9. When to Use Selection Sort

### ✅ Good fit

- **Write-expensive storage** — Flash memory, EEPROM, disk records: O(n) swaps minimises write cycles and wear.
- **Very small arrays** (n < 20) — Overhead of complex algorithms outweighs any gain.
- **Severely memory-constrained** environments where no auxiliary space is available.
- **Educational / embedded contexts** — Simple, predictable, easy to implement correctly.

### ❌ Poor fit

- **Large datasets** — O(n²) is prohibitively slow compared to O(n log n) alternatives.
- **Nearly sorted input** — Insertion sort handles this in O(n); selection sort doesn't adapt.
- **Stability required** — Equal elements may be reordered.
- **Performance-critical code** — Use Timsort, Introsort, or Merge Sort instead.

---

## 10. Alternatives at a Glance

| Algorithm        | Best for                                | Time complexity      |
|------------------|-----------------------------------------|----------------------|
| Insertion sort   | Nearly sorted data, small n, online     | O(n) – O(n²)         |
| Merge sort       | Linked lists, stable O(n log n), large n| O(n log n)           |
| Quick sort       | General purpose, cache-friendly         | O(n log n) average   |
| Heap sort        | Guaranteed O(n log n), in-place         | O(n log n)           |
| Counting sort    | Integer keys in a known range           | O(n + k)             |
| **Selection sort** | Minimal writes, tiny arrays, embedded | **O(n²)**            |

---

## 11. Quick-Reference Summary

```
Algorithm : Selection Sort
Strategy  : Find minimum in unsorted region → swap to front → repeat

Time      : O(n²) — always, no adaptive behaviour
Space     : O(1) — in-place
Swaps     : O(n) — at most n−1 swaps total
Stable    : No
Adaptive  : No

Best when : writes >> reads, or n is very small
Avoid when: large n, nearly sorted data, stability required
```

---

*Notes compiled from the Selection Sort DSA learning session.*
