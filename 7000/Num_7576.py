import sys
from collections import deque
input = sys.stdin.readline

graph = []
queue = deque()
M, N = map(int, input().split())
isEnd = True
for n in range(N):
    line = [int(i) for i in input().split()]
    graph.append(line)
    
    for m in range(M):
        if line[m] == 1:
            queue.append((n, m))
        else:
            isEnd = False

if isEnd:
    print(0)
else:
    actionN = [1, -1, 0, 0]
    actionM = [0, 0, -1, 1]

    while len(queue) > 0:
        n, m = queue.popleft()

        for idx in range(4):
            newN = n + actionN[idx]
            newM = m + actionM[idx]

            if 0 <= newN < N and 0 <= newM < M and graph[newN][newM] == 0:
                graph[newN][newM] = graph[n][m] + 1
                queue.append((newN, newM))

    date = 0
    isCant = False
    for n in range(N):
        for m in range(M):
            if graph[n][m] != 0:
                date = max(graph[n][m], date)
            else:
                isCant = True
                break

    if isCant:
        print(-1)
    else:
        print(date - 1)
