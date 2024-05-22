import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    line = [i for i in input().rstrip()]
    graph.append(line)

countGraph = [[0 for i in range(M)] for _ in range(N)]
countGraph[0][0] = 1
queue = [(0, 0)]
while len(queue) > 0:
    x, y = queue.pop(0)
    if x > 0 and graph[x-1][y] == '1' and countGraph[x-1][y] == 0: # up
        countGraph[x-1][y] = countGraph[x][y] + 1
        queue.append((x-1, y))
    if x < N-1 and graph[x+1][y] == '1' and countGraph[x+1][y] == 0: # down
        countGraph[x+1][y] = countGraph[x][y] + 1
        queue.append((x+1, y))
    if y > 0 and graph[x][y-1] == '1' and countGraph[x][y-1] == 0: # left
        countGraph[x][y-1] = countGraph[x][y] + 1
        queue.append((x, y-1))
    if y < M-1 and graph[x][y+1] == '1' and countGraph[x][y+1] == 0: # right
        countGraph[x][y+1] = countGraph[x][y] + 1
        queue.append((x, y+1))

print(countGraph[N-1][M-1])
