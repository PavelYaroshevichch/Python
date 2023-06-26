import queue
with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    matrix = [list(map(int, row.split())) for row in fin.readlines()]
answer = [-1 for _ in range(n)]
q = queue.Queue()
visited = [False for _ in range(n)]

q.put(0)
visited[0] = True
k = 1
while q.qsize():
    ind = q.get()
    for i in range(n):
        if matrix[ind][i] == 1 and (not visited[i]):
            q.put(i)
            visited[i] = True
    answer[ind] = k + 1
    q.get()
    if q.empty():
        for j in range(n):
            if not visited[j]:
                q.put(j)
                visited[j] = True
                break

with open('output.txt', 'w') as fout:
    print(*answer, file=fout)