import sys

# 입력
N = int(sys.stdin.readline())
graph = [[int(i) for i in sys.stdin.readline().rstrip().split()] for _ in range(N)]

# 능력치 합산
for i in range(N-1):
    for j in range(i+1, N):
        graph[i][j] += graph[j][i]

print(graph) # debug

# 초깃값 설정
visited = [False] * N
visited_team = []
min_abs = 101

# dfs 알고리즘
def dfs(depth: int, next_player: int, value: int):
    if depth == N//2: # 팀원 매칭이 되었을 때
        for bol in visited:
            
        return
    
    visited[next_player] = True
    dfs(depth+1, 1, value+visited[next_player])
        visited[next_player] = False

