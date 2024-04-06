def bfs():
    queue = [[x, y]]

    while len(queue):
        state_x, state_y = queue.pop(0)

        if state_x+1 < M:
            queue.append([state_x+1, state_y])
        if state_y+1 < N:
            queue.append([state_x, state_y+1])
        if state_x-1


for ___ in range(int(input())):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for __ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    warm = 0

    for x in range(N):
        for y in range(M):
            if graph[x][y]:
                @함수