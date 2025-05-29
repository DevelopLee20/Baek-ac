import sys
import heapq

# 표준 입출력 오버라이딩
input = sys.stdin.readline

# 입력
INF = float('inf')
n = int(input())
m = int(input())
graph = [[INF for _ in range(n)] for _ in range(n)]

# 자기자신은 0으로 초기화
for i in range(n):
    graph[i][i] = 0

# 노선 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c) # 중복된 동선 입력 고려

# 플로이드-워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# INF는 0으로 변환
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0

# 출력
for line in graph:
    print(*line, sep=" ")
