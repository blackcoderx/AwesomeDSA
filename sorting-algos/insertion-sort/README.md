# Insertion Sort — Complete DSA Notes

---

## 1. Definition

**Insertion Sort** is a simple, in-place, comparison-based sorting algorithm that builds a sorted array one element at a time. It works similarly to how you would sort a hand of playing cards — you pick one card at a time and insert it into its correct position among the already-sorted cards in your hand.

At any point during execution, the array is divided into two logical parts:

- A **sorted sublist** — on the left, maintained in order.
- An **unsorted sublist** — on the right, waiting to be processed.

On each pass, it takes the next unsorted element (the **key**) and shifts sorted elements rightward until it finds the correct slot, then inserts the key there.

> **Core idea:** Pick the next element → slide sorted elements right to make room → insert it in the correct position → repeat.

---

## 2. Key Properties

| Property         | Value                              |
|------------------|------------------------------------|
| Type             | In-place, comparison sort          |
| Stable           | ✅ Yes                              |
| Adaptive         | ✅ Yes (faster on nearly sorted data)|
| Extra space      | O(1)                               |
| Total swaps      | O(n²) worst case                   |
| Total comparisons| O(n) best — O(n²) worst            |
| Online           | ✅ Yes (can sort as data arrives)   |

---

## 3. How It Works (Step-by-Step)

1. **Start at index 1** — Treat `arr[0]` as a sorted sublist of one element.
2. **Pick the key** — Take `arr[i]` as the element to be inserted.
3. **Find its position** — Compare the key against elements to its left, shifting each one right as long as it is greater than the key.
4. **Insert** — Place the key in the gap left by the shifts.
5. **Advance** — Increment `i` and repeat steps 2–4 until the end of the array.

**Total passes:** n − 1

**Invariant:** After pass *k*, the subarray `arr[0..k]` is sorted. These are not necessarily the *k* smallest elements — they are the first *k+1* elements of the original array, now sorted among themselves.

---

## 4. Example Walkthrough

**Input:** `[12, 11, 13, 5, 6]`

### Pass 1 — key = 11 (i = 1)
```
[12, 11, 13, 5, 6]
     ^
key = 11
12 > 11 → shift 12 right
Insert 11 at index 0

[11, 12, 13, 5, 6]   ✓ Sorted: [11, 12]
```

### Pass 2 — key = 13 (i = 2)
```
[11, 12, 13, 5, 6]
         ^
key = 13
12 < 13 → stop, no shifts needed
13 stays at index 2

[11, 12, 13, 5, 6]   ✓ Sorted: [11, 12, 13]
```

### Pass 3 — key = 5 (i = 3)
```
[11, 12, 13, 5, 6]
             ^
key = 5
13 > 5 → shift right
12 > 5 → shift right
11 > 5 → shift right
Insert 5 at index 0

[5, 11, 12, 13, 6]   ✓ Sorted: [5, 11, 12, 13]
```

### Pass 4 — key = 6 (i = 4)
```
[5, 11, 12, 13, 6]
                ^
key = 6
13 > 6 → shift right
12 > 6 → shift right
11 > 6 → shift right
5 < 6  → stop
Insert 6 at index 1

[5, 6, 11, 12, 13]   ✓ Sorted: [5, 6, 11, 12, 13]
```

**Output:** `[5, 6, 11, 12, 13]` ✅

---

## 5. Implementation

### Python

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]       # Element to be inserted
        j = i - 1         # Start comparing with the element just before key

        # Shift elements greater than key one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key in its correct position
        arr[j + 1] = key

    return arr

# Example
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))  # → [5, 6, 11, 12, 13]
```

### Python — Sorting a list of strings

```python
def insertion_sort_strings(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

words = ["banana", "apple", "cherry", "date"]
print(insertion_sort_strings(words))
# → ['apple', 'banana', 'cherry', 'date']
```

### JavaScript

```javascript
function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        const key = arr[i];
        let j = i - 1;

        // Shift elements greater than key one position to the right
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        // Insert key in its correct position
        arr[j + 1] = key;
    }
    return arr;
}

// Example
console.log(insertionSort([12, 11, 13, 5, 6]));
// → [5, 6, 11, 12, 13]
```

> **Note:** The shift-based approach (`arr[j+1] = arr[j]`) is preferred over swap-based insertion sort. Shifting only writes one value per step; swapping writes two, making it roughly twice as expensive for large elements.

---

## 6. Insertion Sort vs Selection Sort

| Property              | Insertion Sort    | Selection Sort    |
|-----------------------|-------------------|-------------------|
| Time — best case      | **O(n)**          | O(n²)             |
| Time — average case   | O(n²)             | O(n²)             |
| Time — worst case     | O(n²)             | O(n²)             |
| Swaps / shifts        | O(n²) worst case  | **O(n)** always   |
| Space                 | O(1)              | O(1)              |
| Stable                | ✅ Yes             | ❌ No              |
| Adaptive              | ✅ Yes             | ❌ No              |
| Online                | ✅ Yes             | ❌ No              |

**Key insight:** Insertion sort adapts — if the array is already (or nearly) sorted, the inner `while` loop rarely executes, giving O(n) performance. Selection sort always does the full O(n²) scan no matter what.

Selection sort has the edge only when **writes are very expensive** — it makes at most n−1 swaps vs insertion sort's potential O(n²) shifts.

---

## 7. Insertion Sort vs Bubble Sort

| Property              | Insertion Sort    | Bubble Sort       |
|-----------------------|-------------------|-------------------|
| Time — best case      | **O(n)**          | O(n)              |
| Time — average case   | O(n²)             | O(n²)             |
| Time — worst case     | O(n²)             | O(n²)             |
| Stable                | ✅ Yes             | ✅ Yes             |
| Adaptive              | ✅ Yes             | ✅ Yes             |
| Practical speed       | **Faster**        | Slower            |

Both are O(n) on a sorted array, but insertion sort is generally faster in practice because it does fewer comparisons and writes than bubble sort for the same input. Bubble sort's adjacent swaps are less cache-friendly than insertion sort's single-key shifting.

---

## 8. Complexity Analysis

### Time Complexity

**Best case — O(n):** Array is already sorted. The `while` loop never executes (each key is already larger than its predecessor). Only n−1 comparisons are made, one per pass.

**Worst case — O(n²):** Array is sorted in reverse order. Every element must be shifted past all previously sorted elements.

```
Pass 1: 1 comparison
Pass 2: 2 comparisons
...
Pass n−1: n−1 comparisons

Total = 1 + 2 + ... + (n−1) = n(n−1)/2
```

**Average case — O(n²):** On random input, each key shifts about halfway through the sorted sublist, giving n(n−1)/4 comparisons — still Θ(n²).

| Case    | Time Complexity | When                         |
|---------|----------------|------------------------------|
| Best    | O(n)           | Already sorted                |
| Average | O(n²)          | Random order                  |
| Worst   | O(n²)          | Reverse sorted                |

### Space Complexity

**O(1)** — in-place algorithm. Only a constant number of extra variables (`i`, `j`, `key`) are used.

### Comparison and Shift Counts

| n      | Best (comparisons) | Worst (comparisons) | Worst (shifts)  |
|--------|--------------------|---------------------|-----------------|
| 10     | 9                  | 45                  | 45              |
| 100    | 99                 | 4,950               | 4,950           |
| 1,000  | 999                | 499,500             | 499,500         |
| 10,000 | 9,999              | 49,995,000          | 49,995,000      |

---

## 9. Stability

Insertion sort is **stable**. When two elements are equal, the algorithm stops shifting (`arr[j] > key`, not `>=`), so the element already in place stays to the left of the incoming equal key. Their relative order is preserved.

**Example:**
```
Input:  [(3, a), (1, b), (3, c)]
Output: [(1, b), (3, a), (3, c)]
```
Both elements with key `3` maintain their original left-to-right order: `(3, a)` still precedes `(3, c)`. ✅

> **Important:** Using `arr[j] >= key` instead of `arr[j] > key` in the inner loop would break stability. Always use strict greater-than for a stable implementation.

---

## 10. Online Algorithm

Insertion sort is an **online algorithm** — it can sort a list as it receives elements one at a time, without needing the full list upfront.

```python
def online_insertion_sort(sorted_so_far, new_element):
    sorted_so_far.append(new_element)
    j = len(sorted_so_far) - 2
    while j >= 0 and sorted_so_far[j] > new_element:
        sorted_so_far[j + 1] = sorted_so_far[j]
        j -= 1
    sorted_so_far[j + 1] = new_element
    return sorted_so_far

result = []
for x in [5, 2, 8, 1]:
    result = online_insertion_sort(result, x)
    print(result)

# [5]
# [2, 5]
# [2, 5, 8]
# [1, 2, 5, 8]
```

This property makes insertion sort useful for **streaming data** and **maintaining a sorted list** that grows over time.

---

## 11. Binary Insertion Sort (Optimization)

The number of **comparisons** can be reduced using binary search to find the insertion point, giving O(n log n) comparisons. However, the number of **shifts** remains O(n²) since elements still need to be physically moved.

```python
import bisect

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        # Use binary search to find the correct insertion index
        pos = bisect.bisect_left(arr, key, 0, i)

        # Shift elements from pos to i−1 one step to the right
        arr[pos + 1 : i + 1] = arr[pos : i]

        # Insert key at the found position
        arr[pos] = key

    return arr

arr = [12, 11, 13, 5, 6]
print(binary_insertion_sort(arr))  # → [5, 6, 11, 12, 13]
```

| Version              | Comparisons   | Shifts / Writes |
|----------------------|---------------|-----------------|
| Standard             | O(n²)         | O(n²)           |
| Binary insertion sort| O(n log n)    | O(n²)           |

> The practical gain is modest — reducing comparisons helps when comparisons are expensive (e.g. comparing complex objects), but the dominant O(n²) shift cost remains.

---

## 12. When to Use Insertion Sort

### ✅ Good fit

- **Nearly sorted or partially sorted data** — O(n) best case makes it extremely fast here; real-world data is often nearly sorted.
- **Small arrays** (n < 20–50) — Low overhead beats the constant factors of O(n log n) algorithms at small sizes. This is why Timsort and Introsort use insertion sort for small sub-arrays.
- **Online / streaming data** — Can sort a growing list without needing the full dataset.
- **Stable sort required with O(1) space** — One of the few stable in-place O(n²) sorts.
- **Linked lists** — Shifting is O(1) with pointer manipulation; no swapping needed.
- **When simplicity matters** — Trivial to implement correctly; good for embedded or educational contexts.

### ❌ Poor fit

- **Large, random datasets** — O(n²) average case is too slow; use Merge Sort or Quick Sort.
- **Reverse-sorted input at scale** — Worst case hits every time.
- **Write-sensitive storage** — O(n²) shifts make it worse than selection sort in this scenario.

---


## 14. Alternatives at a Glance

| Algorithm          | Best for                                    | Time complexity       |
|--------------------|---------------------------------------------|-----------------------|
| **Insertion sort** | Small n, nearly sorted, online, stable      | **O(n) – O(n²)**     |
| Selection sort     | Minimal writes, tiny arrays                 | O(n²)                 |
| Bubble sort        | Educational, nearly sorted (with flag)      | O(n) – O(n²)          |
| Merge sort         | Stable O(n log n), linked lists, large n    | O(n log n)            |
| Quick sort         | General purpose, cache-friendly             | O(n log n) average    |
| Heap sort          | Guaranteed O(n log n), in-place             | O(n log n)            |
| Timsort            | Real-world data (mixed runs)                | O(n) – O(n log n)     |

---

## 15. Quick-Reference Summary

```
Algorithm   : Insertion Sort
Strategy    : Pick next element → shift sorted elements right → insert → repeat

Time        : O(n) best  |  O(n²) average  |  O(n²) worst
Space       : O(1) — in-place
Stable      : Yes
Adaptive    : Yes — faster on nearly sorted input
Online      : Yes — can process elements one at a time

Best when   : small n, nearly sorted data, streaming, stable sort needed
Avoid when  : large random datasets, write-expensive storage

Used inside : Timsort (Python/Java), Introsort (C++ std::sort), Pdqsort (Rust)
```

---

*Notes compiled as part of the Sorting Algorithms DSA series.*
