A = [5, 2, 4, 6, 1, 3]

def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        index = i-1
        while index >= 0 and A[index] > key:
            # Shift current index value to next index
            A[index+1] = A[index]
            # decrement index by -1
            index -= 1
        A[index+1] = key
    return A


sorted_array = insertion_sort(A)
print("Sorted array", sorted_array)
