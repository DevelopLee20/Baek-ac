'''
1. 3개의 벽 세우기
2. 전염
3. 최종 개수 세기
4. 개수의 최대값 구하기
- 완전 탐색 근거: 시간 제한이 2초, M의 최대값이 정해져 있음
'''
import sys
from copy import deepcopy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

# 입력
N, M = map(int, input().split())

# 리스트 선언
common_graph = []       # 공통으로 사용될 그래프
common_virus_list = []  # 공통으로 사용될 초기 바이러스 위치
empty_list = []         # 빈 공간(벽 세울 공간)
for n in range(N):
    ms = [int(i) for i in input().split()]
    for idx, m in enumerate(ms):
        coordinate = (n, idx)
        if m == 2:
            common_virus_list.append(coordinate)
        elif m == 0:
            empty_list.append(coordinate)

    common_graph.append(ms)

# 이동 가능 방법 4가지(상하좌우)
delta_n_list = [-1, 1, 0, 0]
delta_m_list = [0, 0, -1, 1]

# 세울 수 있는 벽의 조합을 계산
combinations_list = combinations(empty_list, 3)

max_count = 0
for combine in combinations_list:
    queue = deque(common_virus_list)    # 초기 바이러스 가져오기

    graph = deepcopy(common_graph)      # 초기 그래프 상태 가져오기
    for n, m in list(combine):
        graph[n][m] = 1

    while len(queue) > 0:
        n, m = queue.popleft()  # bfs
        for idx in range(4):
            new_n = n + delta_n_list[idx]
            new_m = m + delta_m_list[idx]
            if 0 <= new_n < N and 0 <= new_m < M:
                if graph[new_n][new_m] == 0: # 빈땅이면
                    graph[new_n][new_m] = 2  # 감염
                    queue.append((new_n, new_m))
    
    # 0의 개수 세기
    count = 0
    for mline in graph:
        count += mline.count(0)

    max_count = max(count, max_count)

# 최대 0 개수 반환
print(max_count)
