with open('input.txt', 'r') as fin:
    n, m = fin.readline().split()
    matr = [[0 for _ in range(int(n))] for _ in range(int(n))]
    for s in fin.readlines():
        i, j = s.split()
        i, j = int(i), int(j)
        matr[i - 1][j - 1] = matr[j - 1][i - 1] = 1

with open('output.txt', 'w') as fout:
    for i in matr:
        print(*i, file=fout)


