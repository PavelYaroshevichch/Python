import math
from collections import Counter
# def reorderedPowerOf2(n: int) -> bool:
#     digits = Counter(str(n))
#
#     for i in range(30):
#         if digits == Counter(str(1 << i)):
#             return True
#     return False

def reorderedPowerOf2(n: int) -> bool:
    dict = {}
    num_2 = num = n
    res = 0
    while num != 0:
        res = num % 10
        dict[res] = 0
        num = num // 10

    while num_2 != 0:
        res = num_2 % 10
        dict[res] += 1
        num_2 = num_2 // 10

    for i in range(30):
        dict2 = {}
        num_2 = num = (1 << i)
        res = 0
        while num != 0:
            res = num % 10
            dict2[res] = 0
            num = num // 10

        while num_2 != 0:
            res = num_2 % 10
            dict2[res] += 1
            num_2 = num_2 // 10
        if dict == dict2:
            return True
    return False

print(reorderedPowerOf2(4022))


