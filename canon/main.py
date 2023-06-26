with open("input.txt", 'r') as fin:
    o = int(fin.readline())
    my_dict = {}
    for i in range(o):
        my_dict[i + 1] = 0
    with open("output.txt", 'w') as fout:
        for t in range(o):
            n = [int(t) for t in fin.readline().split()]
            for j in range(o):
                if n[j] == 1:
                    my_dict[j + 1] = t + 1
        for i in sorted(my_dict.keys()):
            print(my_dict[i], end=' ', file=fout)


