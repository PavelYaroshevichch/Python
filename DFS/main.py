with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    matrix = [[int(i) for i in fin.readline().split()] for _ in range(n)]
    def dfs(v, m):
        visited[v] = True
        order[v] = m
        m += 1
        for j in range(n):
            if matrix[v][j] and not visited[j]:
                m = dfs(j, m)
        return m
    with open('output.txt', 'w') as fout:
        index = 1
        visited = [False] * n
        order = [0] * n
        for i in range(n):
            if not visited[i]:
                index = dfs(i, index)
        for i in order:
            fout.write(str(i) + ' ')