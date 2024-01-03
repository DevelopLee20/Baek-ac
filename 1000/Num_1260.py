# 돌다가 방문 false 면 방문 후 true 변경
# 모두 true 일 때 종료

N, M, V = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())

    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

visit = [0 for _ in range(N)]
output = [V]

def search(state):
    visit[state] = 1

    for node, i in enumerate(graph[state]):
        if not visit[node] and i:
            output.append(node+1)
            visit[node] = 1
            search(node)
search(V-1)

print(*output, end="\n")

visit = [0 for _ in range(N)]
visit[V-1] = 1
queue = [V-1]
output = [V]

while len(queue):
    state = queue.pop(0)

    for node, i in enumerate(graph[state]):
        if not visit[node] and i:
            queue.append(node)
            output.append(node+1)
            visit[node] = 1

print(*output, end="")
