import sys

input = sys.stdin.readline
n = int(input())
start, end = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

INF = float('inf')
visited = [INF] * n
visited[start-1] = 0
queue = [(start-1, 0)]
while queue:
    person, cost = queue.pop()
    
    for i in graph[person]:
        if visited[i] > cost + 1:
            visited[i] = cost + 1
            queue.append((i, cost+1))

if visited[end-1] == INF:
    print(-1)
else:
    print(visited[end-1])
