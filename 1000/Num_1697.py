N, K = map(int, input().split())

maxIdx = 100001
graph = [0 for _ in range(maxIdx)]
visited = [False for _ in range(maxIdx)]
queue = [N]

def redfs(current:int, idx: int) -> None:
    if 0 <= idx  <= maxIdx - 1:
        if not visited[idx]:
            visited[idx] = True
            graph[idx] = graph[current] + 1
            queue.append(idx)

while len(queue) > 0:
    current = queue.pop(0)

    if current == K:
        print(graph[current])
        break

    redfs(current, current + 1)
    redfs(current, current - 1)
    redfs(current, current * 2)
