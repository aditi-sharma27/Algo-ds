def max_gap(x):
    max_gap_length = 0
    current_gap_length = 0
    print(x.bit_length(), bin(x))
    for i in range(x.bit_length()):
        if x & (1 << i):
            # Set, any gap is over.
            if current_gap_length > max_gap_length:
                max_gap_length = current_gap_length
            current_gap_length = 0
        else:
            # Not set, the gap widens.
            current_gap_length += 1
    # Gap might end at the end.
    if current_gap_length > max_gap_length:
        max_gap_length = current_gap_length
    return max_gap_length

# print(max_gap(6))

# Can be done using strip() and split() function : Steps:
#
# 1. Convert to binary (Remove first two characters )
# 2. Convert int to string
# 3. Remove the trailing and starting 0 and 1 respectively
# 4. Split with 1 from the string to find the subsequences of strings
# 5. Find the length of the longest substring
# 6. Second strip('1') is not mandatory but it will decrease the cases to be checked and will improve the time complexity Worst case T


def solution(N):
    bin_n = bin(N)[2:]
    num = bin_n.strip('0').strip('1')
    print("strip = ", num)
    return len(max(num.split('1')))

    #return len(max(bin(N)[2:].strip('0').strip('1').split('1')))

print(solution(529))
