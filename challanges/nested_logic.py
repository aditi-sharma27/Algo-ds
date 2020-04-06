# Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:
#
# If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
# If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
# If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
# If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
# Input Format
#
# The first line contains  space-separated integers denoting the respective , , and  on which the book was actually returned.
# The second line contains  space-separated integers denoting the respective , , and  on which the book was expected to be returned (due date).

# Input: 24 10 1776 10 10 1776
# Expected Output:210

# actual_d, actual_m, actual_y = 9, 6, 2015
# exp_d, exp_m, exp_y = 6, 6, 2015
# expected out put = 45

# actual_d, actual_m, actual_y = 8, 4, 2012
# exp_d, exp_m, exp_y = 1, 1, 2011
# expected out put = 10000

# actual_d, actual_m, actual_y = 23, 12, 1234
# exp_d, exp_m, exp_y = 19, 9, 2468
# Expected Output:0

# actual_d, actual_m, actual_y = 24, 10, 1776
# exp_d, exp_m, exp_y = 10, 10, 1776
# # # Expected Output:210

actual_d, actual_m, actual_y = 9, 6, 2015
exp_d, exp_m, exp_y = 19, 2, 2015
# expected out put = 45

def day_diff(a, b, c, x, y, z):
    if z > c:
        yy, m, d = 0, 0, 0
    elif z < c:
        yy = y - c
        m, d = 0, 0
    elif z == c:
        if y > b:
            m, yy = 0, 0
            if x > a:
                d = 0
            elif x < a:
                d = x-a
        elif y < b:
            d, m, yy = 0, b-y, 0
        elif y == b:
            if x > a:
                d, m, yy = 0, 0, 0
            elif x < a:
                d, m, yy = a-x, 0, 0
        elif y == b:
            if x > a:
                d, m, yy = 0, 0, 0
            elif x < a:
                d, m, yy = a-x, 0, 0
            elif x==a:
                d, m, yy = 0, 0, 0
    return d, m, yy


def fine_cal(d, m, y):
    fine = 0
    if y:
        fine = 10000
    elif m:
        fine += 500 * m
    elif d:
        fine += 15 * d
    return fine

d_diff, m_diff, y_diff = day_diff(actual_d, actual_m, actual_y, exp_d,exp_m,exp_y )

f = fine_cal(d_diff, m_diff, y_diff)
print("fine =", f)

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b,c = input().split()
x, y, z = input().split()

def day_diff(a, b, c, x, y, z):
    if z > c:
        yy, m, d = 0, 0, 0
    elif z < c:
        yy = y - c
        m, d = 0, 0
    elif z == c:
        if y > b:
            m, yy = 0, 0
            if x > a:
                d = 0
            elif x < a:
                d = x-a
        elif y < b:
            d, m, yy = 0, b-y, 0
        elif y == b:
            if x > a:
                d, m, yy = 0, 0, 0
            elif x < a:
                d, m, yy = a-x, 0, 0
        elif y == b:
            if x > a:
                d, m, yy = 0, 0, 0
            elif x < a:
                d, m, yy = a-x, 0, 0
            elif x==a:
                d, m, yy = 0, 0, 0
    return d, m, yy


def fine_cal(d, m, y):
    fine = 0
    if y:
        fine = 10000
    elif m:
        fine += 500 * m
    elif d:
        fine += 15 * d
    return fine

d_diff, m_diff, y_diff = day_diff(int(a), int(b), int(c), int(x),int(y), int(z) )

f = fine_cal(d_diff, m_diff, y_diff)
print(f)

"""
