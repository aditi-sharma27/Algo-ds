# Synopsys
# From an array of sorted integers find the closest value to a given number:
# Array: [2, 5, 19, 20, 31, 77, 100]

#  Target : 5
# Output: 5
#  Target : 15
# Output : 19
#  Target : 99
# Output: 100
#  Target : 255
# Output: 100

array = [2, 5, 19, 20, 31, 77, 100]


def find_elem(arr, elem):
    q = int(len(arr)/2)
    left_arr = arr[0:q]
    right_arr = arr[q:]
    diff = []
    if elem < arr[q]:
        for i in range(len(left_arr)):
            if elem == left_arr[i]:
                return elem
            else:
                diff.append(abs(elem-arr[i]))
        min_diff = min(diff)
        for i in range(len(diff)):
            if min_diff == diff[i]:
                return arr[i]
    else:
        for i in range(len(right_arr)):
            if elem == right_arr[i]:
                return elem
            else:
                diff.append(abs(elem-arr[i]))
        min_diff = min(diff)
        for i in range(len(diff)):
            if min_diff == diff[i]:
                return arr[q+i]


print(find_elem(array, 999))
