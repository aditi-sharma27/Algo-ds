# Given two integers,  and , find the maximal value of  xor , written , where  and  satisfy the following condition:
# For example, if  and , then
# Our maximum value is .

l,r = 11, 12
l,r=11,100


def maximizing_xor(l, r):
    print("b",(1 << (len(format(l^r, 'b')))) - 1)

def maximizingXor(l, r):
    return pow(2,len(bin(l^r))-2)-1


a =maximizingXor(l,r)
print("a=", a)
maximizing_xor(l, r)
