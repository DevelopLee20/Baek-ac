import sys
from itertools import combinations

# 입력
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
chicken_site = []
house_site = []
for n in range(N):
    line = list(map(int, input().split()))

    for idx, val in enumerate(line):
        if val == 2: # 치킨집 위치 저장
            chicken_site.append((n, idx))

        elif val == 1: # 집 위치 저장
            house_site.append((n, idx))
    graph.append(line)

# 모든 치킨 거리 계산
city_chicken_length = []
for hx, hy in house_site:
    
    chicken_length = []
    for cx, cy in chicken_site:
        length = abs(hx-cx) + abs(hy - cy)
        chicken_length.append((cx, cy, length))
    
    city_chicken_length.append(sorted(chicken_length, key=lambda x: x[2]))

# 치킨집 조합 계산
min_length = float('inf')
for chicken_combinate in combinations(chicken_site, M):
    value = 0
    for house_chicken_length in city_chicken_length:
        for x, y, length in house_chicken_length:
            if (x, y) in set(chicken_combinate):
                value += length
                break
    min_length = min(min_length, value)

print(min_length)
