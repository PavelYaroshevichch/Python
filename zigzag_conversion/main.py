def convert(s: str, numRows: int):
    lines = ["" for _ in range(numRows)]
    flag = False
    res = ''
    i = j = 0
    n = len(s)
    while j < n:
        lines[i] = lines[i] + s[j]
        if flag == False and i == numRows - 1:
            flag = True
        if flag == True and i == 0:
            flag = False
        if flag == False:
            i = i + 1
        else:
            i = i - 1
        j += 1
    for l in lines:
        res += l.strip()
    res = res.replace(' ', '')
    print(len(res))
    return res



print(convert('''P   A   H   N
                A P L S I I G
                Y   I   R''', 3))