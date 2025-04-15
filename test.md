# 백준 1753 최단경로(골드 4)

링크: [1753 최단경로](https://www.acmicpc.net/problem/1753)

---

## 접근 방법

- 최단거리를 사용하는 알고리즘 사용
- (AI 도움) 다엑스트라 사용
- 다엑스트라는 가중치가 양수일 때 사용 가능
- 최단거리를 찾는 것이기 때문에 사용 가능

---

## 소스 코드

소스 코드: [93152585 제출](https://www.acmicpc.net/source/93152585)

```python
import sys
import heapq

# 입력
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

# 그래프 입력
INF = float('inf')
graph = [[] for _ in range(V)]
for e in range(E):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))

# 다엑스트라 알고리즘으로 최단거리 파악
distance = [INF] * V
distance[K-1] = 0

heap = [(0, K-1)]
while len(heap):
    cost, vertex = heapq.heappop(heap)

    if distance[vertex] < cost:
        continue

    for next_vertex, weight in graph[vertex]:
        next_cost = cost + weight

        if distance[next_vertex] > next_cost:
            distance[next_vertex] = next_cost
            heapq.heappush(heap, (next_cost, next_vertex))

for dis in distance:
    if isinstance(dis, float):
        print("INF")
    else:
        print(dis)
```

---

## 코드 개선 사항

---

## 결론

- 다엑스트라 알고리즘을 학부시절 집중해서 듣지 않았다.. 후회중이다..
- 이번 문제를 계기로 다엑스트라에 익숙해지려 한다.
