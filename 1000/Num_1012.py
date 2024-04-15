'''
T: int 테스트 케이스 개수
M N K
M 가로
N 세로
K 배추 개수

output 최소의 배추흰지렁이 마리 수

field: list
1일때만 bfs를 돌려서 계산 후 0으로 만듬
모두 다 돌면 반복 종료
count: int 배추흰지렁이 세기
상 하 좌 우 인접 노드 방문, 확인했으면 0으로 변경
'''

import sys

input = sys.stdin.readline

def bfs(graph: list, x: int, y: int):
    queue = [[x, y]]
    graph[x][y] = 0

    while len(queue) > 0:
        CurrentX, CurrentY = queue.pop(0)

        if CurrentX+1 < N and graph[CurrentX+1][CurrentY] == 1:
            graph[CurrentX+1][CurrentY] = 0
            queue.append([CurrentX+1, CurrentY])
        if CurrentY+1 < M and graph[CurrentX][CurrentY+1] == 1:
            graph[CurrentX][CurrentY+1] = 0
            queue.append([CurrentX, CurrentY+1])
        if CurrentX-1 >= 0 and graph[CurrentX-1][CurrentY] == 1:
            graph[CurrentX-1][CurrentY] = 0
            queue.append([CurrentX-1, CurrentY])
        if CurrentY-1 >= 0 and graph[CurrentX][CurrentY-1] == 1:
            graph[CurrentX][CurrentY-1] = 0
            queue.append([CurrentX, CurrentY-1])

T = int(input())
for _ in range(T): # 가로 M, 세로 N -> N=x, M=y
    M, N, K = map(int, input().split(" "))
    field = [[0 for __ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split(" "))
        field[y][x] = 1

    count = 0
    for x in range(M):
        for y in range(N):
            if field[y][x] == 1:
                bfs(field, y, x)
                count += 1

    print(count)
