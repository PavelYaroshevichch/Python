n, k = [int(t) for t in input().split()]
matr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    matr[i][i] = 1
    matr[i][0] = 1
for i in range(1, n + 1):
    for j in range(i):
        matr[i][j] = matr[i - 1][j - 1] + matr[i - 1][j]
if k == n:
    print(1)
elif k == 0 or n == 0:
    print(1)
else:
    print(matr[n][k] % (pow(10, 9) + 7))




