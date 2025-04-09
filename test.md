# 백준 10844 쉬운 계단 수

링크: [10844 쉬운 계단 수](https://www.acmicpc.net/problem/10844)

---

## 접근 방법

- (시간 초과) dfs로 반복해서 해당 길이에 도달했을 때 반복 종료
- (성공) dp로 각 단계에서 생성될 수 있는 개수를 세기

---

## 소스 코드 1 (시간 초과)

소스 코드: [92876897 제출](https://www.acmicpc.net/source/92876897)

```python
from collections import deque

N = int(input()) # 입력
count = 0

queue = deque([i for i in range(1, 10)])
while len(queue) > 0:
    number = queue.pop()

    if number // 10**(N-1) > 0:
        count += 1
        continue

    last_number = number % 10

    if last_number - 1 >= 0:
        new_number = number * 10 + (last_number - 1)
        queue.append(new_number)
    if last_number + 1 < 10:
        new_number = number * 10 + (last_number + 1)
        queue.append(new_number)

print(count)
```

- O(2^N)의 시간이 소비되어 완전 탐색 방법은 N=100 이상일 경우 시간 초과가 발생한다는 것을 알았다.

## 소스 코드 2

소스 코드: [92879617 제출](https://www.acmicpc.net/source/92879617)

```python
# 입력
N = int(input())

# 초기값 설정(1~9의 경우의 수는 1가지, 0은 0가지)
dp = [[0 for _ in range(10)] for _ in range(N)]
for idx in range(1, 10):
    dp[0][idx] = 1

# 반복으로 dp 리스트 작성
for n in range(1, N):
    dp[n][0] = dp[n-1][1] % 1000000000

    for num in range(1, 9):
        dp[n][num] = (dp[n-1][num-1] + dp[n-1][num+1]) % 1000000000

    dp[n][9] = dp[n-1][8] % 1000000000

# 최종합계 출력
print(sum(dp[N-1]) % 1000000000)
```

- dp로 변경해서 해결

---

## 결론

- 완전 탐색이 N=100 이상이면 시간 초과가 발생한다는 것과 시간 1초 이상 소요된다는 것을 이해하고 다른 방법을 사용할 수 있도록 빠르게 생각하는 방법을 공부해야될 것 같다.
