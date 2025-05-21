import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]

delta_r = [0, 0, 1, -1]
delta_c = [1, -1, 0, 0]

visited = [False for _ in range(26)]
visited[65 - ord(graph[0][0])] = True
max_count = 0
def dfs(r:int, c:int):
    global max_count
    max_count = max(max_count, sum(visited))
    
    for dr, dc in zip(delta_r, delta_c):
        new_r = r + dr
        new_c = c + dc
        
        if 0 <= new_r < R and 0 <= new_c < C and not visited[65 - ord(graph[new_r][new_c])]:
            visited[65 - ord(graph[new_r][new_c])] = True
            dfs(new_r, new_c)
            visited[65 - ord(graph[new_r][new_c])] = False

dfs(0, 0)
print(max_count)
