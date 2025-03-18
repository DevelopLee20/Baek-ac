# 입력
N, K = map(int, input().split())
graph = [int(i) for i in input().split()]

# 초깃값 설정
dp = [0] * (N-K+1)
dp[0] = sum(graph[0:K])

# 최댓값 계산
for idx in range(K, N):
    dp[idx-K+1] = dp[idx-K] - graph[idx-K] + graph[idx]

# 출력
print(max(dp))
