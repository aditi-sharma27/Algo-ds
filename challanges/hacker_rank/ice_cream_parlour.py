

def ice_cream_parlor(m, arr):
    for i in range(len(arr)-1):
        for j in range(1, len(arr)):
            sum = arr[i]+arr[j]
            if sum == m:
                print(arr[i], arr[j])
                #return arr[i], arr[i+1]

# m1=5
# array = [1, 4, 5, 3, 2]
# m1= 4
# array = [2, 2, 4, 3]
m1=6
array = [1, 3, 4, 5, 6]

result = ice_cream_parlor(m1, array)
print(result)
