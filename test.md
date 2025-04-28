# 백준 9465 스티커 (실버 1)

링크: [9465 스티커](https://www.acmicpc.net/problem/9465)

---

## 접근 방법

- 위 또는 아래 또는 선택하지 않음을 선택하고 다음 칸으로 넘어간다고 생각하면 dp로 풀 수 있을 것 같음

---

## 소스 코드

소스 코드: [dp 풀이 정답 소스 코드](https://www.acmicpc.net/source/93667017)

```python
import sys

input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())

    score = []
    for _ in range(2):
        score.append(list(map(int, input().split())))

    dp = [[0 for _ in range(n+1)] for _ in range(2)]

    for i in range(1, n+1):
        dp[0][i] = max(dp[1][i-1] + score[0][i-1], dp[0][i-1])
        dp[1][i] = max(dp[0][i-1] + score[1][i-1], dp[1][i-1])
    
    print(max(dp[0][n], dp[1][n]))
```

---

## 코드 개선 사항(GPT 4o)

```python
# 전
dp = [[0 for _ in range(n+1)] for _ in range(2)]

# 후
dp = [[0 for _ in range(n)] for _ in range(2)]
```

- 배열 크기를 n+1로 할 필요 없음(이전에 작성하던 문제풀이 방식을 이어 생각하다보니 헷갈린듯)

---

```python
# 전
score = []
for _ in range(2):
    score.append(list(map(int, input().split())))

# 후
score = [list(map(int, input().split())) for _ in range(2)]
```

- 더 직관적이고 깔끔하게 코드 바꾸기
- 사실 이 방법을 생각하다가 구현하지 못해서 사용하지 못한 방식

```python
dp = [[0] * n for _ in range(2)]
```

- 이 방식도 가능하다.

## 결론

- dp 인 것을 바로 알아차렸고, 문제를 쉽게 풀 수 있었다.
- 이 문제는 슬라이싱 윈도우 방식으로도 풀 수 있어서 dp 리스트를 사용하지 않고도 풀 수 있다.
- 계속 이상함을 느낀 부분이 바로 이부분 이었는 듯
