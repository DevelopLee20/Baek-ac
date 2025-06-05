N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N)]
for i in range(10):
    dp[0][i] = 1

for n in range(1, N):
    for i in range(10):
        for j in range(0, i+1):
            dp[n][i] = (dp[n][i] + dp[n-1][j]) % 10007

print(sum(dp[-1]) % 10007)
