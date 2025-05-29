# 백준 11404 플로이드 (골드 4)

링크: [11404 플로이드](https://www.acmicpc.net/problem/11404)

---

## 접근 방법

- (시간초과) 비용이 양수이고, 최소 비용 구하기는 다익스트라
- (도움) 모든 출발 지점에서의 비용을 고려해야할 땐, 플로이드-워셜 알고리즘을 사용한다.

---

## 소스 코드

소스 코드: [플로이드-워셜 알고리즘](https://www.acmicpc.net/source/94881618)

```python
import sys
import heapq

# 표준 입출력 오버라이딩
input = sys.stdin.readline

# 입력
INF = float('inf')
n = int(input())
m = int(input())
graph = [[INF for _ in range(n)] for _ in range(n)]

# 자기자신은 0으로 초기화
for i in range(n):
    graph[i][i] = 0

# 노선 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c) # 중복된 동선 입력 고려

# 플로이드-워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# INF는 0으로 변환
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0

# 출력
for line in graph:
    print(*line, sep=" ")
```

---

## 코드 개선 사항(GPT 4o)

```python
```

- 없음

## 결론

- 다익스트라에 익숙해져서 무작정 썼다가 피봤다..
- 플로이드-워셜 알고리즘은 모든 경우의 최소비용을 구할 때 유용하다.
- 아이디어는 직접가는 것보다 경유해서 가는 것이 비용이 더 쌀 수 있다는 것에서 시작
