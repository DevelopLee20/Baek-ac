# 백준 11660 구간 합 구하기 5 (실버 1)

링크: [11660 구간 합 구하기 5](https://www.acmicpc.net/problem/11660)

---

## 접근 방법

- 같은 값을 M번 계산할 수 있으므로 dfs bfs는 사용불가
- sum 연산을 하는 것은 속도가 느릴 것
- 특정 범위의 값을 미리 계산해두고 꺼내쓰기

---

## 소스 코드

소스 코드: [제출한 정답 소스 코드](https://www.acmicpc.net/source/93452912)

```python
import sys

# 표준입출력 방식 변경
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
graph = [[int(i) for i in input().split()] for _ in range(N)]

# 구간 합 방식으로 계산
prefix = [[0] * (N+1) for _ in range(N+1)]
for row in range(1, N+1):
    for col in range(1, N+1):
        # 왼쪽과 위 값을 더한 후 중복된 부분을 빼기
        prefix[row][col] = graph[row-1][col-1] + prefix[row-1][col] + prefix[row][col-1] - prefix[row-1][col-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]
    print(result)
```

---

## 코드 개선 사항(GPT 4o)

```python
# 전
graph = [[int(i) for i in input().split()] for _ in range(N)]

# 후
graph = [list(map(int, input().split())) for _ in range(N)]
```

- 리스트를 작성할 때 map이 좀 더 빠르다고 합니다.

---

## 결론

- 나름 문제를 분석하는 시간을 많이 가지고 시작해서 나름 쉽게 문제를 푼 것 같은데 분할정복으로 헷갈려서 바로 못풀었다.
- 아쉽다..
