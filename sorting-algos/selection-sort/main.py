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
