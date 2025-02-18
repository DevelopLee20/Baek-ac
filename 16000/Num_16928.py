import sys
import collections

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [i for i in range(101)]

for _ in range(N):
    start, end = map(int, input().split())

    graph[start] = end

for _ in range(M):
    start, end = map(int, input().split())

    graph[start] = end

visited = [0] * 101
queue = collections.deque([1])
visited[1] = 1
while len(queue) > 0:
    state = queue.popleft()
    # print("state:", state) # Debug

    for action in range(state+1, state+7):
        new_state = graph[action]

        if not visited[new_state]:
            if new_state == 100:
                print(visited[state])
                exit()

            visited[new_state] = visited[state] + 1
            queue.append(new_state)
