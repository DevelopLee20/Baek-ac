N = int(input())
A = list(map(int, input().split()))

dp = [1] * (N)
for t in range(N):
    for c in range(t):
        if A[c] > A[t]:
            dp[t] = max(dp[c] + 1, dp[t])

print(max(dp))
