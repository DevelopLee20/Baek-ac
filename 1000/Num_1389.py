'''
유저 N: edge 개수
친구 관계 M: node 개수
모두 연결되어 있다.
모두 연결하는데, 짧은 연결만 허용
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0 for i in range(N)] for i in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1 # idx라서 -1 해준다.
    graph[y-1][x-1] = 1 # idx라서 -1 해준다.

resultGraph = [[0 for i in range(N)] for i in range(N)]
for startIdx in range(N):
    visited = [0 for i in range(N)]
    queue = [startIdx]
    visited[startIdx] = True
    count = 1
    addCount = 1
    newCount = 0

    while len(queue) > 0:
        edge = queue.pop(0)
        addCount -= 1

        for idx, connect in enumerate(graph[edge]):
            if connect and visited[idx] == 0:
                visited[idx] = True
                resultGraph[startIdx][idx] = count
                queue.append(idx)
                newCount += 1

        if addCount == 0:
            addCount = newCount
            newCount = 0
            count += 1

minIdx = 0
for idx in range(1, N):
    if sum(resultGraph[minIdx]) > sum(resultGraph[idx]):
        minIdx = idx

print(minIdx+1)
