

def icecreamParlor(m, a):
    arr = sorted(a)
    print(arr)
    for i in range(len(arr)-1):
        sum = arr[i]+arr[i+1]
        if sum ==m:
            return arr[i], arr[i+1]


array = [1, 4, 5, 3, 2]
m1= 4
array = [2, 2, 4, 3]
m1=6
array = [1, 3, 4, 5, 6]

result = icecreamParlor(m1, array)
print(result)
