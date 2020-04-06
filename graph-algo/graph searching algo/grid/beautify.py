
n = 12122
arr = list(map(int, str(n)))
print(arr)


def beauty(arr, num):
    index_arr = []
    for i in range(len(arr)):
        if arr[i] == num:
            index_arr.append(i)
    for i in range(len(index_arr)-1):
        print(abs(index_arr[i])-abs(index_arr[i+1]))

beauty(arr, 2)
