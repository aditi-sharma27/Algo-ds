#For a given array of repeated elements, exactly one element is not repeated. You need to return the non-repeated element.
"""You will be given an array of integers. All of the integers except one occur twice. That one is unique in the array.

Given an array of integers, find and print the unique element.

For example, , the unique element is .
Complete the lonelyinteger function in the editor below. It should return the integer which occurs only once in the input array.

lonelyinteger has the following parameter(s):

a: an array of integers"""
from functools import reduce

A = [1, 2, 3, 4, 3, 2, 1]
print(reduce(int.__xor__, A))


# approach 2
def lonely_integer(arr):
    v = 0
    for i in arr:
        v = i ^ v
    print(v)

lonely_integer(A)
