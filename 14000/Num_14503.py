import sys

# 입력
N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 시뮬레이션
def simulate(r: int, c: int, d: int) -> int:
    action = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    clean_set = set()

    while True:
        if graph[r][c] == 0 and (r, c) not in clean_set:
            clean_set.add((r, c))

        is_clean = False # 청소 했음

        for _ in range(4):
            d = (d + 3) % 4
            new_x = r + action[d][0]
            new_y = c + action[d][1]

            if (0 <= new_x < N and 0 <= new_y < M) and (new_x, new_y) not in clean_set and graph[new_x][new_y] == 0:
                r, c = new_x, new_y
                is_clean = True
                break
        
        if not is_clean:
            new_x = r + action[(d+2) % 4][0]
            new_y = c + action[(d+2) % 4][1]

            if graph[new_x][new_y] == 1:
                return len(clean_set)

            r, c = new_x, new_y

print(simulate(r, c, d))
