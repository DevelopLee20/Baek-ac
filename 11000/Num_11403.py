'''
주제: 방향 그래프, 깊이 우선 탐색법
문제: 양수인 경로가 있는지 없는지?
방문 -> 방문체크, 다음위치 탐색(연결 and 미방문)
방문 리스트 반환
'''
import sys

N = int(input())
graph = []
for _ in range(N):
    row = [i for i in map(int, sys.stdin.readline().split())]
    graph.append(row)

visited = [[0 for x in range(N)] for y in range(N)]
for node in range(N):
    stack = []
    for idx, edge in enumerate(graph[node]):
        if edge == 1 and visited[node][idx] == 0:
            stack.append(idx)
            visited[node][idx] = 1
    
    while len(stack):
        state = stack.pop()

        for idx, edge in enumerate(graph[state]):
            if edge == 1 and visited[node][idx] == 0:
                stack.append(idx)
                visited[node][idx] = 1

for idx in range(N):
    print(*visited[idx])
