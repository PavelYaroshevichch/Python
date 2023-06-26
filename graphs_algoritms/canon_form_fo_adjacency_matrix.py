with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    matrix = [list(map(int, row.split())) for row in fin.readlines()]
    canon_form = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                continue
            else:
                canon_form[j] = i + 1

with open('output.txt', 'w') as fout:
    print(*canon_form, file=fout)
