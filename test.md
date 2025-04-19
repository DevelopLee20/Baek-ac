# 백준 15686 치킨 배달 (골드 5)

링크: [15686 치킨 배달](https://www.acmicpc.net/problem/15686)

---

## 접근 방법

- 각 집마다 치킨 집의 위치와 거리를 오름차순으로 저장
- 가능한 치킨집 조합을 계산
- 치킨집 조합과 위치가 동일한지 판단 후 오름차순 하나씩 탐색

---

## 소스 코드

소스 코드: [93340693 제출](https://www.acmicpc.net/source/93340693)

```python
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
            if (x, y) in chicken_combinate:
                value += length
                break
    min_length = min(min_length, value)

print(min_length)
```

---

## 코드 개선 사항(GPT 4o)

```python
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
```

- combinations는 list를 반환하는데, 순차 탐색을 해야될 경우 set()을 활용하여 탐색 속도를 O(n)에서 O(1)로 줄인다.
- 그 이유는 set()은 해쉬 테이블 구조이기 때문이다.

---

## 결론

- 구조물을 통과할 수 없는 줄 알고 2시간 가량 시간초과를 잡는데 시간을 소모했다..
- 구조물 없이 거리만을 계산하는 것을 맨해튼 거리라고 한다.
- 후... 역시 2시간은 힘들다..
