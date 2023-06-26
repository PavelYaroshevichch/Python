def isPalindrome(x):
    flag = True
    res = 0
    num = x
    while x != 0:
        x = x // 10
        res += 1
    temp = res
    num_f = num_l = num
    for i in range(res // 2 + 1):
        first = num_f // pow(10, temp - 1)
        num_f = num_f % pow(10, temp - 1)
        temp -= 1
        last = num_l % 10
        num_l = num_l // 10
        if first == last:
            continue
        else:
            flag = False
    return flag
print(isPalindrome(10061))