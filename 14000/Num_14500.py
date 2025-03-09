import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
    line = [int(i) for i in input().split()]
    graph.append(line)

# 움직이는 경우의 수 설정
delta_n = [1, -1, 0, 0]
delta_m = [0, 0, 1, -1]

# 출력할 최대값
max_value = 0

# 방문 확인
visited = [[False for _ in range(M)] for _ in range(N)]

def dfs(x, y, depth, value):
    global max_value

    # 테트로미노 완성시 종료
    if depth == 4:
        max_value = max(max_value, value)
        return
    
    # 테트로미노 경우의 수 탐색
    for idx in range(4):
        dx = x + delta_n[idx]
        dy = y + delta_m[idx]

        # 범위를 벗어나지 않는지 판단 및 방문 확인
        if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy]:
            visited[dx][dy] = True
            dfs(dx, dy, depth+1, value+graph[dx][dy])
            visited[dx][dy] = False

def special_shape(x, y):
    global max_value
    
    shapes = [
        [(0, 0), (-1, 0), (0, -1), (0, 1)],  # ㅗ
        [(0, 0), (1, 0), (0, -1), (0, 1)],   # ㅜ
        [(0, 0), (1, 0), (-1, 0), (0, 1)],   # ㅏ
        [(0, 0), (1, 0), (-1, 0), (0, -1)]   # ㅓ
    ]
    for shape in shapes:
        total = 0
        for dx, dy in shape:
            if 0 <= x + dx < N and 0 <= y + dy < M:
                total += graph[x + dx][y + dy]
            else:
                continue

        max_value = max(max_value, total)

# DFS 각 시작점마다 반복
for n in range(N):
    for m in range(M):
        visited[n][m] = True
        dfs(n, m, 1, graph[n][m])
        visited[n][m] = False
        special_shape(n, m)

print(max_value)
