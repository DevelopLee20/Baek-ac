import sys
import heapq

# 표준 입력 오버라이딩
input = sys.stdin.readline

# 입력
N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
for m in range(M):
    v1, v2, cost = map(int, input().split())
    graph[v1-1].append((v2-1, cost))

start, end = map(int, input().split())

# 다엑스트라 알고리즘
INF = float('inf')
distance = [INF] * N
distance[start-1] = 0

heap = [(start-1, 0)] # 최소힙
while len(heap):
    vertex, cost = heapq.heappop(heap)
    
    if distance[vertex] < cost:
        continue
    
    # 현재 정점에서 가능한 다른 정점 확인
    for next_vertex, weight in graph[vertex]:
        next_cost = cost + weight
        
        # 기존의 비용보다 적을 경우 갱신
        if distance[next_vertex] > next_cost:
            distance[next_vertex] = next_cost
            heapq.heappush(heap, (next_vertex, next_cost))

# 출력
print(distance[end-1])
