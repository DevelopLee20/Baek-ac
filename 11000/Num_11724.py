import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for x in range(N)]
for m in range(M):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

visited = []
count = 0
for idx in range(N):
    if idx not in visited:
        queue = [idx]
        visited.append(idx)
        count += 1

        while len(queue):
            now = queue.pop(0)

            for nxt in graph[now]:
                if nxt not in visited:
                    visited.append(nxt)
                    queue.append(nxt)

print(count)
