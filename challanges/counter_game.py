

hg_num = 8


def check_for_power_of2(num):
    result = bin(num)
    if result.count('1') == 1:
        print("No {} is in power of 2 and count is {}".format(num, result.count('1')))
        return True
    else:
        print("No {} isn't in power of 2 and count is {}".format(num, result.count('1')))
        return False


def louise(num):
    result = check_for_power_of2(num)
    if result:
        if int(num/2) == 1:
            print("Louise win")
        else:
            richard(int(num/2))
    else:
        new_num = num - 2**(len(bin(num)[2:])-1)
        richard(new_num)


def richard(num):
    result = check_for_power_of2(num)
    if result:
        if int(num/2) == 1:
            print("Richard win")
        else:
            louise(int(num/2))
    else:
        louise(num - 2**(len(bin(num)[2:])-1))


louise(6)
