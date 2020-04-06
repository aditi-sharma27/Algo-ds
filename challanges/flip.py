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

    A = [0, 0, 1]
    A = [0,0,0,1,0,1,0,1,1,1]
    #print(get_flip_count(str))
    print(min(flip_opr(A, 0), flip_opr(A, 1)))
