'''
M: 가로
N: 세로
H: 높이
익은 토마토 1
익지 않은 토마토 0
없는 칸 -1
M을 N 만큼 입력, H 만큼 반복
'''
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = []
for h in range(H):
    box = []
    for n in range(N):
        line = input().rstrip().split()
        box.append(line)
    graph.append(box)

new_queue = []
visited = [[[0 for m in range(M)] for n in range(N)] for h in range(H)]

already = H * N * M
for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 1:
                new_queue.append((h, n, m))
                already -= 1

print("Debug:", new_queue)

if not already:
    print(0)
else:
    count = 0
    while len(new_queue):
        queue = new_queue.copy()
        new_queue = []
        count += 1

        while len(queue):
            h, n, m = queue.pop(0)
            visited[h][n][m] = 1

            if h+1 < H and visited[h+1][n][m] != 1:
                if graph[h+1][n][m] == 0:
                    new_queue.append((h+1, n, m))
                elif graph[h+1][n][m] == -1:
                    visited[h+1][n][m] = 1
            if h > 0 and visited[h-1][n][m] != 1:
                if graph[h-1][n][m] == 0:
                    new_queue.append((h-1, n, m))
                elif graph[h-1][n][m] == -1:
                    visited[h-1][n][m] = 1
            if n+1 < N and visited[h][n+1][m] != 1:
                if graph[h][n+1][m] == 0:
                    new_queue.append((h, n+1, m))
                elif graph[h][n+1][m] == -1:
                    visited[h][n+1][m] = 1
            if n > 0 and visited[h][n-1][m] != 1:
                if graph[h][n-1][m] == 0:
                    new_queue.append((h, n-1, m))
                elif graph[h][n-1][m] == -1:
                    visited[h][n-1][m] = 1
            if m+1 < M and visited[h][n][m+1] != 1:
                if graph[h][n][m+1] == 0:
                    new_queue.append((h, n, m+1))
                elif graph[h][n][m+1] == -1:
                    visited[h][n][m+1] = 1
            if m > 0 and visited[h][n][m-1] != 1:
                if graph[h][n][m-1] == 0:
                    new_queue.append((h, n, m-1))
                elif graph[h][n][m-1] == -1:
                    visited[h][n][m-1] = 1

    allVisited = True
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if visited[h][n][m] != 1:
                    allVisited = False
    
    if allVisited:
        print(count)
    else:
        print(-1)

print(visited)
