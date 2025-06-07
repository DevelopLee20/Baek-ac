N = int(input())
N_list = list(map(int, input().split()))

dp = [[1, 1] for _ in range(N)]

for i in range(N):
    for j in range(i):
        if N_list[i] > N_list[j]: # 수열 증가
            dp[i][0] = max(dp[i][0], dp[j][0]+1)
        if N_list[i] < N_list[j]: # 수열 감소 및 수열 증가했다가 감소
            dp[i][1] = max(dp[i][1], dp[j][1]+1, dp[j][0]+1)

print(max(max(dp[i]) for i in range(N)))
