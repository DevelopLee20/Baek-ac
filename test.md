# 백준 7562 나이트의 이동 (실버 1)

링크: [7562 나이트의 이동](https://www.acmicpc.net/problem/7562)

---

## 접근 방법

- dp로 모든 내용을 기록해가면서 가장 짧은 거리를 찾기
  - 해당 내용은 과정상 시간 초과가 발생할 것으로 예상
- (힌트) bfs로 최단 거리를 파악하여 해결

---

## 소스 코드

소스 코드: [BFS 소스 코드](https://www.acmicpc.net/source/93875697)

```python
from collections import deque

T = int(input())

delta_x = [2, 2, 1, -1, -2, -2, 1, -1]
delta_y = [1, -1, 2, 2, 1, -1, -2, -2]

def bfs_loop() -> int:
    L = int(input())
    
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    if x1 == x2 and y1 == y2:
        return 0

    graph = [[-1] * L for _ in range(L)]
    queue = deque()
    queue.append((x1, y1))
    graph[x1][y1] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(delta_x, delta_y):
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < L and 0 <= new_y < L:
                if new_x == x2 and new_y == y2:
                    return graph[x][y] + 1
                elif graph[new_x][new_y] == -1:
                    graph[new_x][new_y] = graph[x][y] + 1
                    queue.append((new_x, new_y))

for t in range(T):
    print(bfs_loop())
```

---

## 코드 개선 사항(GPT 4o)

```python
# 전
delta_x = [2, 2, 1, -1, -2, -2, 1, -1]
delta_y = [1, -1, 2, 2, 1, -1, -2, -2]

# 후
directions = [
        (2, 1), (2, -1), (1, 2), (-1, 2),
        (-2, 1), (-2, -1), (1, -2), (-1, -2)
    ]
```

- 리스트로 관리하는 것보다 튜플로 묶어서 관리하는 것이 용이함

```python
# 전
graph = [[-1] * L for _ in range(L)]

# 후
visited = [[False] * L for _ in range(L)]
queue = deque([(start[0], start[1], 0)])  # (x, y, moves)
visited[start[0]][start[1]] = True
```

- 나는 graph 변수에 visited와 횟수를 동시에 저장했지만, 그러지 말고 구분해서 명확히 하는 것이 더 직관적임
- 특히 queue 튜플에 변수를 하나 더 넣어서 이동 횟수를 저장하는 것을 추천

## 결론

- 처음 문제를 풀기 전 키보드를 치워두고 노트와 펜만으로 어떻게 접근해야할지 결정하고 시작하는데, 이 과정에서 시간을 너무 소비한 것 같고, 간단한 BFS 문제인지 파악하지 못해서 아쉽게 느껴지는 문제였다.
