with open('input.txt', 'r') as fin:
    n, m = [int(x) for x in fin.readline().split()]
    matr = [[] for _ in range(n)]
    for s in fin.readlines():
        i, j = list(map(lambda x: int(x), s.split()))
        matr[i - 1].append(j)
        matr[j - 1].append(i)

with open('output.txt', 'w') as fout:
    for arr in matr:
        print(len(arr), end=' ', file=fout)
        print(*arr, file=fout)



