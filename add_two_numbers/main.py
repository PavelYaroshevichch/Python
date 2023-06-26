from collections import deque
l_1 = deque([3, 4, 5])
l_2 = deque([5, 4, 2])
l_answer = deque()
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(l1, l2):
    suma = 0
    num = len(l1)
    for i, j in zip(l1, l2):
        suma += (i + j) * pow(10, num - 1)
        num -= 1
    res = 0
    suma_2 = suma
    answer = 0
    while suma != 0:
        suma = suma // 10
        res += 1
    res_2 = res
    while res != 0:
        temp = suma_2 % 10
        answer += temp * pow(10, res - 1)
        suma_2 = suma_2 // 10
        res -= 1
    while res_2 != 0:
        temp_2 = answer // pow(10, res_2 - 1)
        l_answer.append(temp_2)
        if answer // pow(10, res_2 - 2) == 0:
            l_answer.append(temp_2)
            res -= 2
        else:
            answer = answer % pow(10, res_2 - 1)
            res_2 -= 1

    return l_answer
print(addTwoNumbers(l_1, l_2))

