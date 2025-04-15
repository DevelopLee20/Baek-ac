import sys
from collections import deque
from copy import deepcopy

# 입력
V, E = map(int, sys.stdin.readline().split())
K = int(input())

graph = [[] for _ in range(V)]
# 간선 입력 후 비용 작성
for e in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u-1].append(v-1, w)

# 간선만큼 반복해서 최솟값 저장
INF = float('inf')
visited = [INF for _ in range(V)]
# 제자리는 비용 0
visited[v-1] = 0

queue = deque([])
for v, cost in enumerate(graph[K-1]):
    if v > 0:
        queue.append((v, cost))
        visited[K-1][v] = True

while len(queue) > 0:
    vertex, cost = queue.popleft()

    for v in range(V):
        if not visited[vertex][v] and graph[vertex][v] != -1:
            visited[vertex][v] = True
            if graph[K-1][v] == -1:
                graph[K-1][v] = graph[vertex][v] + cost
            elif graph[vertex][v] + cost < graph[K-1][v]:
                graph[K-1][v] = graph[vertex][v] + cost
            else:
                continue

            cost += graph[vertex][v]
            queue.append((v, cost))


# 최솟값 출력
for cost in graph[K-1]:
    if cost == -1:
        print("INF")
    else:
        print(cost)
