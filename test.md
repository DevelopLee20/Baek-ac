# 백준 11052 카드 구매하기 (실버 1)

링크: [11052 카드 구매하기](https://www.acmicpc.net/problem/11052)

---

## 접근 방법

- (틀렸습니다) 카드 팩의 평균 가격 정렬 후 구매
- (정답) DP로 풀이

---

## 소스 코드

소스 코드: [다이나믹 프로그래밍 소스 코드](https://www.acmicpc.net/source/94670772)

```python
# 입력
N = int(input())
cost_list = list(map(int, input().split()))

# 다이나믹 프로그래밍 알고리즘 수행
dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(i):
        dp[i] = max(dp[j] + cost_list[i-j-1], dp[i])

print(dp[N])
```

---

## 코드 개선 사항(GPT 4o)

```python
```

- 없음

## 결론

- 이게 그리디 알고리즘으로는 시간초과가 발생할 것 같은데, 논리적으로 틀린 부분은 모르겠다..
- 요즘 GPT도 무료 버전은 조금 상태가 안좋은 듯...
