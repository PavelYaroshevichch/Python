with open('input.txt', 'r') as fin:
    m, c, n = [int(t) for t in fin.readline().split()]
    array = [int(i) for i in fin.readlines()]


def hash_func(key, i):
    return ((key % m) + c * i) % m


def hash_table(array):
    hash_table = [-1 for t in range(m)]
    i = 0
    for key in array:
        res = hash_func(key, i)
        if hash_table[res] == -1:
            hash_table[res] = key
        else:
            while hash_table[res] != -1:
                i += 1
                res = hash_func(key, i)
            i = 0
            hash_table[res] = key


    return hash_table





with open('output.txt', 'w') as fout:
    for i in hash_table(array):
        print(str(i), end=' ', file=fout)


