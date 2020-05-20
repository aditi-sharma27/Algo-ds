# Linkedin
import math
import os
import random
import re
import sys


def divisible_pair_sum(elem_list, k):
    counter = 0
    for i, elem in enumerate(elem_list):
        j = i+1
        while j < len(elem_list):
            summ = elem_list[i] + elem_list[j]
            if summ % k == 0:
                counter += 1
            j += 1
    return counter


if __name__ == '__main__':
    nk = input().split()
    print("nk=", nk)
    n = int(nk[0])

    k = int(nk[1])

    a = list(map(int, input().rstrip().split()))
    b = divisible_pair_sum(a, k)
    print(b)
