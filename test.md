# 백준 2293 동전 1 (골드 4)

링크: [2293 동전 1](https://www.acmicpc.net/problem/2293)

---

## 접근 방법

- 제한 시간이 0.5초이므로 dp로 중간 과정을 저장하면서 간다.

---

## 소스 코드

소스 코드: [다이나믹 프로그래밍 소스 코드](https://www.acmicpc.net/source/94301422)

```python
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1
for val in n_list:
    for i in range(val, k+1):
        dp[i] += dp[i - val]

print(dp[-1])
```

---

## 코드 개선 사항(GPT 4o)

```python
```

- 없다.

## 결론

- DP라는 것을 충분히 인지하였으나, 마무리와 디테일이 부족해서 도움을 받았다 ㅜㅜ
- 많이 아쉽다..
