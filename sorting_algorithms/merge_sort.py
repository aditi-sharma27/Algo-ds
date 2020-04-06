
import math


A = [2, 4, 5, 7, 1, 2, 3, 6]
def merge(arr, p, q, r):
    # calculate indexes for new sub array
    n1 = q - p
    n2 = r - q
    print(n1, n2)
    # define left and right sub array
    left_arr, right_arr = [], []
    for i in range(q+1):
        left_arr.append(arr[i])
    for i in range(q+1, r+1):
        right_arr.append(arr[i])
    left_arr.append(math.inf)
    right_arr.append(math.inf)
    print(left_arr, right_arr)

    i, j = 0, 0
    # iterate
    for k in (range(r+1)):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
    print(arr)


def merge_sort(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

merge_sort(A, 0, 7)
