a = ["11", "4", "5", "2"]

elem = map(int, a)
b=[]
for i in elem:
    b.append(i)

b.sort()
print(b[0])

#
# def add(a,b):
#     assert(a>b)
#     assert(b>a)
#     print(a/b)
# add(4,0)

list1=[34,24,112,25]
list2 = list1
del list1
print ("list = ", list2)


b = 0
for a in range(0, 5, 2):
    b += a + 1
    print (b)

x = [12,2,3,[14,23]]
y = x[:]
y[3][0] = 13
print (x)

variable = 5
def print_function(variable=variable):
    print(variable)
variable=6
print_function(8)
print_function()
print(variable)
