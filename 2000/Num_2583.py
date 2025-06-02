import sys

# 입력
input = sys.stdin.readline
M, N, K = map(int, input().split())
graph = [[False for _ in range(N)] for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            if not graph[y][x]:
                graph[y][x] = True

# dfs
action = ((0, 1), (1, 0), (0, -1), (-1, 0))
def dfs(x: int, y: int) -> int:
    queue = [(x, y)]
    graph[x][y] = True
    extent = 1
    
    while queue:
        x, y = queue.pop()
        for dx, dy in action:
            next_x = x + dx
            next_y = y + dy
            
            if 0 <= next_x < M and 0 <= next_y < N and not graph[next_x][next_y]:
                graph[next_x][next_y] = True
                queue.append((next_x, next_y))
                extent += 1
    
    return extent

# main
area = 0
extents = []
for x in range(M):
    for y in range(N):
        if not graph[x][y]:
            extent = dfs(x, y)
            extents.append(extent)
            area += 1

# 출력
print(area)
print(*sorted(extents))
