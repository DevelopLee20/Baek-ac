import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
in_graph = [0] * N
for m in range(M):
    A, B = map(int, input().split())
    graph[A-1].append((B-1, 1))
    in_graph[B-1] += 1

# 앞에 있는 수가 없을 때
queue = []
for idx, val in enumerate(in_graph):
    if val == 0:
        queue.append(idx)
        in_graph[idx] = -1

output = []
while queue:
    idx = queue.pop()
    output.append(idx+1)
    
    for i, val in graph[idx]:
        in_graph[i] -= 1
        
        if in_graph[i] == 0:
            queue.append(i)
            in_graph[i] = -1

print(*output, sep=" ")
