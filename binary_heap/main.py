with open('input.txt', 'r') as fin:
    counter = int(fin.readline())
    value = [int(i) for i in fin.readline().split()]
with open('output.txt', 'w') as fout:
    j = 0
    while j * 2 + 1 < counter:
        if 2 * j + 2 < counter:
            if value[j] > value[2 * j + 1] or value[j] > value[2 * j + 2]:


                fout.write('NO')
                break
        else:
            if value[j] > value[2 * j + 1]:


                fout.write('NO')
                break
        j += 1
    fout.write("YES")

