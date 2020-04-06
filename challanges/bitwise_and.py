A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4, 5, 6, 7, 8]
C = [1, 2]


def bit_wise_max_value(my_list, k):
    bit_value = []
    for i, num in enumerate(my_list):
        j = i + 1
        while j < len(my_list):
            bit_value.append(my_list[i] & my_list[j])
            j += 1
    #print("new bit value", bit_value)
    for _ in bit_value:
        max_value = max(bit_value)
        if max_value < k:
            return max_value
        else:
            bit_value.remove(max_value)


def bit_wise_max_value1(n, k):
    if k-1|k<=n:
        print(k-1|k)
        print(k-1)
    else:
        print(k-2)

    #print(k-1 if (k-1)|k <= n else k-2)

a = bit_wise_max_value1(5, 2)



for _ in range(int(input())):
    n, k = [int(i) for i in input().strip().split()]
    print(k-1 if (k-1)|k <= n else k-2)


