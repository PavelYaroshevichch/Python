with open('in.txt', 'r') as fin:
    n = int(fin.readline())
    array_moves = [int(t) for t in fin.read().split()]
my_set = set()
x = 0
y = 0
flag = False
my_tuple = (0, 0)
my_set.add(my_tuple)
for i in range(n):
    if array_moves[i] == 0:
        y += 1
        my_tuple = (x, y)
    elif array_moves[i] == 1:
        x += 1
        y += 1
        my_tuple = (x, y)
    elif array_moves[i] == 2:
        x += 1
        my_tuple = (x, y)
    elif array_moves[i] == 3:
        x += 1
        y -= 1
        my_tuple = (x, y)
    elif array_moves[i] == 4:
        y -= 1
        my_tuple = (x, y)
    elif array_moves[i] == 5:
        x -= 1
        y -= 1
        my_tuple = (x, y)
    elif array_moves[i] == 6:
        x -= 1
        my_tuple = (x, y)
    elif array_moves[i] == 7:
        x -= 1
        y += 1
        my_tuple = (x, y)
    len1 = len(my_set)
    my_set.add(my_tuple)
    len2 = len(my_set)
    print(my_tuple)
    if len1 == len2:
        flag = True
        break
    else:
        continue
with open('out.txt', 'w') as fout:
    if flag == True:
        fout.write('Yes')
    else:
        fout.write('No')




