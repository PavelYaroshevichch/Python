import numpy as np
def diagonalSort(mat):
    n, m = np.shape(mat)
    if m % 2 == 0:
        res = 2 * m - 2
        matr_sort = [[] for _ in range(res)]
    else:
        res = 2 * m - 2
        matr_sort = [[] for _ in range(res)]

    for i in range(n):
        for j in range(m):
            matr_sort[i - j].append(mat[i][j])

    for i in range(res):
        matr_sort[i].sort(reverse=True)

    for i in range(n):
        for j in range(m):
            mat[i][j] = matr_sort[i - j].pop()
    return mat




print(diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))