with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    canon_form = [0 for _ in range(n)]
    for s in fin.readlines():
        i, j = list(map(lambda x: int(x), s.split()))
        canon_form[j - 1] = i

with open('output.txt', 'w') as fout:
    print(*canon_form, file=fout)