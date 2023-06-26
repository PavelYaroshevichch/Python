def premax(key, list):
    end = len(list)
    start = 0
    while end > start:
        middle = int((end + start) // 2)
        if key <= list[middle]:
            end = middle
        elif key > list[middle]:
            start = middle + 1
    return start

def binaryarch(key, list):
    end = len(list)
    start = 0
    while end > start:
        middle = int((end + start) // 2)
        if key == list[middle]:
            return 1
        elif key < list[middle]:
            end = middle
        elif key > list[middle]:
            start = middle + 1
    return 0


def max(key, list):
    end = len(list)
    start = 0
    while end > start:
        middle = int((end + start) // 2)
        if key < list[middle]:
            end = middle
        elif key >= list[middle]:
            start = middle + 1
    return start
power = 0
list1 = []
keys = []
power = int(input())
string_for_list = input()
for t in string_for_list.split():
    try:
        list1.append(int(t))
    except ValueError:
        pass
power_keys = int(input())
string_for_find = input()
for t in string_for_find.split():
    try:
        keys.append(int(t))
    except ValueError:
        pass


for i in range(power_keys):
    result = keys[i]
    print(str(binaryarch(result, list1)), end=' ')
    print(str(premax(result, list1)), end=' ')
    print(str(max(result, list1)), end='\n')
