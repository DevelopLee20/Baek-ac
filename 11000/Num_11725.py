'''
1트: 메모리 초과 문제 발생
해결방안: output 리스트와 visited를 합침

2트: 메모리 초과 문제 발생
해결방안: 인터넷 검색으로 알아냄, 0이 너무 많아서 graph를 희소행렬 처럼 0을 생략해 표현
'''

import sys

# input을 대체
input = sys.stdin.readline

# N 입력
N = int(input())

# 너비 우선 탐색을 위한 그래프 선언
graph = [[] for _ in range(N)]

# 방문 여부와 함께 부모 노드를 저장할 리스트 선언
visited = [0 for _ in range(N)]

# N-1 정점 입력
for _ in range(N-1):
    x, y = map(int, input().split())

    # 양방향 노드로 연결
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

# 루트 노드부터 너비우선 탐색 진행
queue = [1]
visited[0] = 1

# 너비 우선 탐색
while len(queue) > 0:
    node = queue.pop(0)

    for idx in graph[node-1]:
        if not visited[idx]:
            queue.append(idx+1)

            # 루트 노드를 저장
            visited[idx] = node

# 출력 양식에 맞게 출력
print(*visited[1:], sep="\n")
