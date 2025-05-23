# 입력
N = int(input())
cost_list = list(map(int, input().split()))

# 다이나믹 프로그래밍 알고리즘 수행
dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(i):
        dp[i] = max(dp[j] + cost_list[i-j-1], dp[i])

# 출력
print(dp[N])
