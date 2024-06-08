n = int(input())

dp = [0, 1] + [0] * (n-1)
for idx in range(2, n+1):
    dp[idx] = dp[idx-2] + dp[idx-1]

print(dp[n])
