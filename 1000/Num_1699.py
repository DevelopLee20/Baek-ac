N = int(input())

dp = [float('inf')] * (N+1)
dp[0] = 0
n_list = [i*i for i in range(1, int(N**0.5)+1)]
for i in range(N):
    for n in n_list:
        if i + n <= N:
            dp[i+n] = min(dp[i+n], dp[i] + 1)
        else:
            break

print(dp[N])
