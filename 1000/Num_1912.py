n = int(input())
n_list = [int(i) for i in input().split(" ")]

dp = [0] * n
dp[0] = n_list[0]

for idx in range(n):
    if dp[idx-1] > 0:
        dp[idx] = dp[idx-1] + n_list[idx]
    else:
        dp[idx] = n_list[idx]

print(max(dp))
