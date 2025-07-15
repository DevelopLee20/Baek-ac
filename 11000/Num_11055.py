# 입력
N = int(input())
A = list(map(int, input().split()))

# DP 알고리즘
dp = [0] * N

for i in range(N):
    dp[i] = A[i]
    for j in range(i):
        if A[j] < A[i] and (dp[j] + A[i]) > dp[i]:
            dp[i] = dp[j] + A[i]

# 출력
print(max(dp))
