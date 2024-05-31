'''
M: 가로
N: 세로
H: 높이
익은 토마토 1
익지 않은 토마토 0
없는 칸 -1
M을 N 만큼 입력, H 만큼 반복
'''
from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = []
queue = deque()

for h in range(H):
    layer = []
    for n in range(N):
        line = [int(i) for i in input().rstrip().split()]
        layer.append(line)

        for m in range(M):
            if line[m] == 1:
                queue.append((h, n, m))
    
    graph.append(layer)

# 상, 하, 좌, 우, 위칸, 아래칸
actionH = [0, 0, 0, 0, -1, 1]
actionN = [-1, 1, 0, 0, 0, 0]
actionM = [0, 0, -1, 1, 0, 0]

while len(queue) > 0:
    h, n, m = queue.popleft()

    for idx in range(6):
        newH = h + actionH[idx]
        newN = n + actionN[idx]
        newM = m + actionM[idx]

        if 0 <= newH < H and 0 <= newN < N and 0 <= newM < M and graph[newH][newN][newM] == 0:
            graph[newH][newN][newM] = graph[h][n][m] + 1
            queue.append((newH, newN, newM))

visitMax = 0
isEnd = True
for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 0:
                isEnd = False
            visitMax = max(graph[h][n][m], visitMax)

if isEnd:
    print(visitMax - 1)
else:
    print(-1)
