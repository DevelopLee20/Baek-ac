import sys
from collections import deque

# 입력
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

# 방문처리 (안뚫고, 뚫고)
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

# bfs 기본 변수 설정
queue = deque()
queue.append((0, 0, 1, 0))
visited[0][0][0] = 1

# bfs 알고리즘
while queue:
    x, y, move, crash = queue.popleft()

    if x == N - 1 and y == M - 1: # bfs라서 가장 빨리 도착한 것이 최단거리
        print(move)
        exit()

    for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < N and 0 <= new_y < M: # 유효한 좌표인지 검증
            if graph[new_x][new_y] == 0 and not visited[new_x][new_y][crash]:   # 칸이 0 이고, 방문하지 않았을 때
                visited[new_x][new_y][crash] = True         # 방문처리
                queue.append((new_x, new_y, move+1, crash)) # 이동

            elif graph[new_x][new_y] == 1 and crash == 0 and not visited[new_x][new_y][1]: # 칸이 1 이고, 부술 수 있으며, 부순 동선에 방문하지 않았을 때
                visited[new_x][new_y][1] = True         # 방문처리
                queue.append((new_x, new_y, move+1, 1)) # 이동, 부순 동선으로 처리
print(-1)
