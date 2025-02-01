import sys

N = int(sys.stdin.readline())
cost = []
for _ in range(N):
    r, g, b = map(int, sys.stdin.readline().split(" "))
    cost.append([r, g, b])

dp = [[0, 0, 0] for _ in range(N)]
dp[0] = cost[0]

for index in range(1, N):
    dp[index][0] = cost[index][0] + min(dp[index-1][1], dp[index-1][2])
    dp[index][1] = cost[index][1] + min(dp[index-1][0], dp[index-1][2])
    dp[index][2] = cost[index][2] + min(dp[index-1][0], dp[index-1][1])

print(min(dp[-1]))
