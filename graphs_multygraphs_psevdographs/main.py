with open("input.txt", 'r') as fin:
    graph = False
    graph1 = True
    graph2 = True
    graph3 = False
    multygraph = False
    multygraph1 = True
    psevdograph = True
    my_set = set()
    f, s = [int(t) for t in fin.readline().split()]
    matr = [[] for i in range(s)]
    for i in range(s):
        matr[i] = [int(t) for t in fin.readline().split()]
    for i in range(s):
        if matr[i][0] == matr[i][1]:
            graph2 = False
            multygraph1 = False
        else:
            graph = True
            multygraph = True
        size1 = len(my_set)
        my_tuple1 = (matr[i][0], matr[i][1])
        my_tuple2 = (matr[i][1], matr[i][0])
        my_set.add(my_tuple1)
        my_set.add(my_tuple2)
        size2 = len(my_set)
        if size2 - size1 < 2:
            graph1 = False
        else:
            graph = True
    with open("output.txt", 'w+') as fout:
        if graph == True and graph1 == True and graph2 == True:
            graph3 = True
            fout.write('Yes' + '\n')
        else:
            fout.write('No' + '\n')
        if graph3 == True:
            fout.write('Yes' + '\n')
        elif multygraph == True and multygraph1 == True:
            fout.write('Yes' + '\n')
        else:
            fout.write('No' + '\n')
        fout.write('Yes' + '\n')