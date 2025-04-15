import sys
import heapq

# 입력
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

# 그래프 입력
INF = float('inf')
graph = [[] for _ in range(V)]
for e in range(E):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))

# 다엑스트라 알고리즘으로 최단거리 파악
distance = [INF] * V
distance[K-1] = 0

heap = [(0, K-1)]
while len(heap):
    cost, vertex = heapq.heappop(heap)

    if distance[vertex] < cost:
        continue

    for next_vertex, weight in graph[vertex]:
        next_cost = cost + weight

        if distance[next_vertex] > next_cost:
            distance[next_vertex] = next_cost
            heapq.heappush(heap, (next_cost, next_vertex))

for dis in distance:
    if isinstance(dis, float):
        print("INF")
    else:
        print(dis)
