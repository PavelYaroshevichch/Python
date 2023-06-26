with open("input.txt", 'r') as fin:
    o, s = [int(t) for t in fin.readline().split()]
    my_dict = {}
    for i in range(o):
        my_dict[i + 1] = []
    with open("output.txt", 'w+') as fout:
        for _ in range(s):
            i, j = [int(t) for t in fin.readline().split()]
            my_dict[j].append(i)
            my_dict[i].append(j)
        for i in sorted(my_dict.keys()):
            print(len(my_dict[i]), *my_dict[i], file=fout)


