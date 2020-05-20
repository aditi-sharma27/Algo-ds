# Python 3 program to find minimum number of
# flip to make binary string alternate

# Utility method to flip a character
def flip(ch):
    return '1' if (ch == '0') else '0'


def flip_opr(arr, next_value):
    count = 0
    for i in arr:
        # inc count if flip opr required
        if i != next_value:
            count += 1
        # get next value
        if next_value == 0:
            next_value = 1
        else:
            next_value = 0
    return count

if __name__ == "__main__":

    A = [0, 0, 0, 0, 0, 1]
    #A = [0,0,0,1,0,1,0,1,1,1]
    #A = [0, 1, 1, 1, 0, 0]
    #print(get_flip_count(str))
    #print(min(flip_opr(A, 0), flip_opr(A, 1)))
    print(A)
    co = 0
    co1 = 0
    for i in range(len(A)-1):
        res = A[i] ^ A[i+1]
        if res == 0 and A[0] == 1:
            #print(A[i+1], A[i+1] >> 1)
            co += 1
            A[i+1] = 1 - A[i+1]
            print(A, co)


    print(co, co1)


