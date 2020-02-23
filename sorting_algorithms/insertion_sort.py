A = [5, 2, 4, 6, 1, 3]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        index = i-1
        while index >= 0 and arr[index] > key:
            # Shift current index value to next index
            arr[index+1] = arr[index]
            # decrement index by -1
            index -= 1
        arr[index+1] = key
    return arr


sorted_array = insertion_sort(A)
print("Sorted array", sorted_array)
