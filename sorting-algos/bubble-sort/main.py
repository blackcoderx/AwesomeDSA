print("Hello Bubble Sorting 🫧")


def bubble_sort(arr: list) -> list:
    n: int = len(arr)  # get the lenght of the array

    for i in range(n - 1):  # Number of passes
        print(i)
        swapped: bool = False

        for j in range(0, n - i - 1):  # Shrinks each pass (last i elements are sorted)
            print(f"before swap {arr}")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                print(f"After swap {arr}")
                swapped = True

        if not swapped:
            break

    return arr


# Example
arr = [1, 2, 3, 5, 8]
# arr = [5, 3, 8, 1, 2]
op = bubble_sort(arr=arr)

print(f"Sorted Array  is {op}")
