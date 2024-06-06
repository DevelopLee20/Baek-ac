import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
queue = []
for n in range(N):
    nLine = list(i for i in input().rstrip())
    graph.append(nLine)

    for m in range(M):
        if nLine[m] == 'I':
            queue.append((n, m))
            graph[n][m] = 1
    

count = 0
actionX = [1, -1, 0, 0]
actionY = [0, 0, 1, -1]
while len(queue) > 0:
    x, y = queue.pop(0)

    for i in range(4):
        new_x = x + actionX[i]
        new_y = y + actionY[i]

        if 0 <= new_x < N and 0 <= new_y < M and 'X' != graph[new_x][new_y] != 1:
            if graph[new_x][new_y] == "P":
                count += 1
            
            queue.append((new_x, new_y))
            graph[new_x][new_y] = 1

if count:
    print(count)
else:
    print("TT")
