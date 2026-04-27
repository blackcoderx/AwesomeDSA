def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be inserted
        j = i - 1  # Start comparing with the element just before key

        # Shift elements greater than key one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key in its correct position
        arr[j + 1] = key

    return arr


# Example
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))
