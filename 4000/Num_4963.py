import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append([int(i) for i in input().split(" ")])

    visited = [[0 for _ in range(w)] for _ in range(h)]
    count = 0
    for x in range(w):
        for y in range(h):
            if graph[y][x] == 1 and not visited[y][x]:
                count += 1
                
                queue = deque()
                queue.append([y, x])
                while len(queue) > 0:
                    state_y, state_x = queue.popleft()
                    visited[state_y][state_x] = 1

                    for i in range(8):
                        new_y, new_x = state_y + dy[i], state_x + dx[i]

                        if 0 <= new_y < h and 0 <= new_x < w and not visited[new_y][new_x] and graph[new_y][new_x] == 1:
                            queue.append((new_y, new_x))
                            visited[new_y][new_x] = 1

    print(count)
