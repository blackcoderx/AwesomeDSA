# Bubble Sort in Python

## What is Bubble Sort?

Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares **adjacent elements**, and swaps them if they're in the wrong order. Larger elements "bubble up" to the end with each pass.

---

## How It Works (Step-by-Step)

Given: `[5, 3, 8, 1, 2]`

**Pass 1:**
```
[5, 3, 8, 1, 2] → compare 5,3 → swap  → [3, 5, 8, 1, 2]
[3, 5, 8, 1, 2] → compare 5,8 → no swap
[3, 5, 8, 1, 2] → compare 8,1 → swap  → [3, 5, 1, 8, 2]
[3, 5, 1, 8, 2] → compare 8,2 → swap  → [3, 5, 1, 2, 8] ✅ 8 is in place
```
Each pass places the **next largest element** at its correct position.

---

## Basic Implementation

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):               # Number of passes
        for j in range(0, n - i - 1):  # Shrinks each pass (last i elements are sorted)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap

    return arr

# Example
arr = [5, 3, 8, 1, 2]
print(bubble_sort(arr))  # Output: [1, 2, 3, 5, 8]
```

---

## Optimized Implementation (Early Exit)

If no swaps occur in a pass, the array is already sorted — no need to continue.

```python
def bubble_sort_optimized(arr):
    n = len(arr)

    for i in range(n):
        swapped = False  # 🔑 Optimization flag

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:  # No swaps = already sorted → break early
            break

    return arr

# Already sorted array — exits after 1 pass instead of n passes
arr = [1, 2, 3, 4, 5]
print(bubble_sort_optimized(arr))  # Output: [1, 2, 3, 4, 5]
```

---

## Visual Trace

```
Initial:  [5, 3, 8, 1, 2]

Pass 1:   [3, 5, 1, 2, 8]   ← 8 bubbles to end
Pass 2:   [3, 1, 2, 5, 8]   ← 5 bubbles to position
Pass 3:   [1, 2, 3, 5, 8]   ← 3 bubbles to position
Pass 4:   [1, 2, 3, 5, 8]   ← no swaps → done ✅
```

---

## Time & Space Complexity

| Case | Time Complexity | When? |
|------|----------------|-------|
| **Best** | O(n) | Already sorted (optimized version) |
| **Average** | O(n²) | Random order |
| **Worst** | O(n²) | Reverse sorted |
| **Space** | O(1) | In-place sorting |

---

## Key Characteristics

| Property | Value |
|----------|-------|
| **Stable** | ✅ Yes (equal elements maintain order) |
| **In-place** | ✅ Yes (no extra memory) |
| **Adaptive** | ✅ Yes (optimized version) |
| **Best use case** | Small or nearly sorted datasets |

---

## When to Use / Avoid

✅ **Use when:**
- Dataset is small
- Almost sorted data
- Simplicity is priority (teaching/learning)

❌ **Avoid when:**
- Large datasets → prefer **Quick Sort O(n log n)** or **Merge Sort O(n log n)**
- Performance is critical

Bubble Sort is rarely used in production but is a great foundation for understanding sorting algorithms!
