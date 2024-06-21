'''
인접한 값을 하나로 묶는 것
좌표, 색상
action은 상하좌우
'''
import sys

N = int(input())
graph = []
visited = []
visited2 = []
for row in range(N):
    r = [col for col in sys.stdin.readline().rstrip()]
    graph.append(r)
    visited.append([0 for _ in range(N)])
    visited2.append([0 for _ in range(N)])

actionX = [1, -1, 0, 0]
actionY = [0, 0, 1, -1]
def bfs(state, color):
    queue = [state]

    while len(queue) > 0:
        x, y = queue.pop(0)
        
        for idx in range(4):
            newX = x + actionX[idx]
            newY = y + actionY[idx]

            if 0 <= newX < N and 0 <= newY < N:
                if graph[newX][newY] == color and visited[newX][newY] == 0:
                    visited[newX][newY] = 1
                    queue.append((newX, newY))

def bfs2(state, color):
    queue = [state]

    while len(queue) > 0:
        x, y = queue.pop(0)
        
        for idx in range(4):
            newX = x + actionX[idx]
            newY = y + actionY[idx]

            if 0 <= newX < N and 0 <= newY < N:
                if color in ['R','G']:
                    if graph[newX][newY] in ['R','G'] and visited2[newX][newY] == 0:
                        visited2[newX][newY] = 1
                        queue.append((newX, newY))
                else:
                    if graph[newX][newY] == color and visited2[newX][newY] == 0:
                        visited2[newX][newY] = 1
                        queue.append((newX, newY))

areaCount = 0
rgAreaCount = 0
for x in range(N):
    for y in range(N):
        if visited[x][y] == 0:
            visited[x][y] = 1
            bfs((x, y), graph[x][y])
            areaCount += 1
        
        if visited2[x][y] == 0:
            visited2[x][y] = 1
            bfs2((x, y), graph[x][y])
            rgAreaCount += 1

print(areaCount, rgAreaCount)
