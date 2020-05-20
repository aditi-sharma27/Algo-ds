"""A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000]."""

A = [3, 1, 2, 4, 3]
    #3, 4, 2, 1, 3
#A = [2, 2002]
#A=[1,2]
#A=[5, 2, 8]
A = [5, 10, 15, 20, 52]
left = A[0]
right = sum(A) - A[0]
m = abs(left-right)
for i in range(1, len(A)-1):
    left += A[i]
    right -= A[i]
    print(A[i], left, right)
    m = min(abs(left - right), m)
print(m)


def solution(A):
    s = sum(A)
    m = float('inf')
    #print("sum, m =", s, m)
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        #print(i, left_sum, 2*left_sum, s - 2*left_sum)
        #print(abs(s - 2*left_sum), m)
        m = min(abs(s - 2*left_sum), m)
    return m
#print(solution(A))

