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
