# A Python program to check if a string is 'n' times
# repetition of one of its substrings

# A utility function to fill lps[] or compute prefix funcrion
# used in KMP string matching algorithm. Refer
# https://www.geeksforgeeks.org/archives/11902 for details

def evaluate_str(string, M, lps):
    length = 0        # length of the previous longest prefix suffix
    i = 1

    lps[0] = 0    # lps[0] is always 0

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        print("i, m(len) , lps, length", i, M, lps, length)
        if string[i] == string[length]:
            print("str = len")
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                print("Special case yes")
                # This is tricky. Consider the example AAACAAAA
                # and i = 7.
                length = lps[length-1]
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
    print("lps = ",lps)
# Returns true if string is repetition of one of its substrings
# else return false.
def isRepeat(string):
    n = len(string)
    lps = [0] * n
    evaluate_str(string, n, lps)

    # Find length of longest suffix which is also
    # prefix of str.
    length = lps[n-1]
    print("longest suffix = ", n, length, lps, lps[n-1])
    print("longest prefix = ", n/(n-len))
    # If there exist a suffix which is also prefix AND
    # Length of the remaining substring divides total
    # length, then str[0..n-len-1] is the substring that
    # repeats n/(n-len) times (Readers can print substring
    # and value of n/(n-len) for more clarity.
    #print("length = ", int(n / (n-length)), n % (n-length), n, n-length)
    print(string, length)
    # print("n =", n, length, string[:str_mo])
    if n > 0 and n % (n-length) == 0:
        print("final ", string[:n-length])
        return True
    else:
        False

# Driver program
txt = ["ABCABC", "ABABAB", "ABCDABCD", "GEEKSFORGEEKS",
        "GEEKGEEK", "AAAACAAAAC", "ABCDABC"]
txt= "abcxabc"
txt = "abcababcababcab"
txt = "AAAACAAAAC"
txt = "abababababab"
print(txt)
n = len(txt)
a = isRepeat(txt)
print(a)
# for i in xrange(n):
#     if isRepeat(txt[i]):
#         print "True"
#     else:
#         print "False"
