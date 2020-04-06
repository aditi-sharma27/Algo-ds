
S= 1234567891
X = 5
K =10

def find_no(x, k, s):
    array = []
    arr = list(map(int, str(s)))
    arr_no = int(len(str(S))/x)
    print(arr, arr_no)
    final = [arr[i * x:(i + 1) * x] for i in range((len(arr) + x - 1) // x)]
    elem = len(final)
    print(elem, final)
    for i in range(len(final[0])-1):
        for j in range(len(final[i])):
            print("elem =", final[i][i], final[i+1][j])
            array.append(int(str(final[i][i])+str(final[i+1][j])))

    print(array)





find_no(X, K, S)

