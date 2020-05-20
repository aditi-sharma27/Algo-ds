#Problem-statement
"""Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting
 the maximum number of consecutive 's in 's binary representation."""


def consecutive_ones(n):
    counter = 0
    while n:
        n &= (n << 1)
        counter += 1
    print(counter)
    return counter


#consecutive_ones(7)

# reducing the count of no of consecutive onces. once it reaches to zero we can count the no of ietration to get maxm no of consecutive onces.


def consecutive_ones(n):
    counter = 0
    while n:
        n &= (n << 1)
        counter += 1
    print(counter)
    return counter


string1 = 'aaaaabb'
no = string1.replace('a', '1')
no = no.replace('b', '0')
print(no)
consecutive_ones(int(no))
#???? do for string
