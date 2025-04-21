import sys

# 입력
input = sys.stdin.readline
N = int(input())
graph = []
max_height = 0
for _ in range(N):
    line = [int(i) for i in input().split()]
    graph.append(line)
    
    max_height = max(max(line), max_height) # 최대 높이 구하기

# dfs
delta_x = [1, -1, 0, 0]
delta_y = [0, 0, 1, -1]
def dfs(visited: set, height: int, start_x: int, start_y: int):
    queue = [(start_x, start_y)]
    visited.add((start_x, start_y))

    while len(queue) > 0:
        x, y = queue.pop()

        for i in range(len(delta_x)):
            new_x = x + delta_x[i]
            new_y = y + delta_y[i]

            if 0 <= new_x < N and 0 <= new_y < N:
                if (new_x, new_y) not in visited and graph[new_x][new_y] > height:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))

# 높이와 지점 설정
max_safe_area = 1
for height in range(1, max_height):
    visited = set()
    safe_area = 0

    for x in range(N):
        for y in range(N):
            if graph[x][y] > height and (x, y) not in visited:
                dfs(visited, height, x, y)
                safe_area += 1

    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)
