import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
queue = []
for N in range(n):
    line = [i for i in map(int, input().split())]
    for idx, M in enumerate(line):
        if line[idx] == 2:
            queue.append((N, idx))
            line[idx] = 0
    graph.append(line)

distance = [[0 for M in range(m)] for N in range(n)]
actionX = [-1, 1, 0, 0]
actionY = [0, 0, -1, 1]
while len(queue) > 0:
    x, y = queue.pop(0)

    for i in range(4):
        new_x = x + actionX[i]
        new_y = y + actionY[i]

        if 0 <= new_x < n and 0 <= new_y < m and (new_x, new_y) and graph[new_x][new_y]:
            distance[new_x][new_y] = distance[x][y] + 1
            queue.append((new_x, new_y))
            graph[new_x][new_y] = 0

for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            distance[x][y] = -1

for n in distance:
    print(*n)
