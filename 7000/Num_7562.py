from collections import deque

T = int(input())

delta_x = [2, 2, 1, -1, -2, -2, 1, -1]
delta_y = [1, -1, 2, 2, 1, -1, -2, -2]

def bfs_loop() -> int:
    L = int(input())
    
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    if x1 == x2 and y1 == y2:
        return 0

    graph = [[-1] * L for _ in range(L)]
    queue = deque()
    queue.append((x1, y1))
    graph[x1][y1] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(delta_x, delta_y):
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < L and 0 <= new_y < L:
                if new_x == x2 and new_y == y2:
                    return graph[x][y] + 1
                elif graph[new_x][new_y] == -1:
                    graph[new_x][new_y] = graph[x][y] + 1
                    queue.append((new_x, new_y))

for t in range(T):
    print(bfs_loop())
