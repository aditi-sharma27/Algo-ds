
# concept
# something_true and x -> x
# something_false and x -> something_false
# something_true or x -> something_true
# something_false or x -> x

my_list1 = [None]
if my_list1:
    print("True")

my_list2 = [False]
if my_list2:
    print("True")

my_list1 = [True,  True,  True, False,  True]
my_list2 = [False, True, False,  True, False]

result = my_list1 and my_list2
print("result", result)

print(None and True)
