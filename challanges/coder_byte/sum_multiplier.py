arr = [2, 5, 6, -6, 16, 2, 3, 6, 5, 3]
arr = [2, 2, 2, 2, 4, 1]
arr = [1, 1, 2, 10, 3, 1, 12]
arr = [2, 1000]

def sum_mul():
    if arr:
        max_sum = 2 * sum(arr)
        max_no = max(arr)
        print(max_sum, max_no)
        arr.remove(max_no)
        second_max = max(arr)
        print(max_no, second_max, max_sum)

        if max_no * second_max > max_sum:
            #print("True", True)
            return True
        else:
            #print("False", False)
            return False
    else:
        print("False", False)
        return False


print("res", sum_mul())

# ok
