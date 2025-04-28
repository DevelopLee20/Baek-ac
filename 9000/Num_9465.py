import sys

input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())

    score = []
    for _ in range(2):
        score.append(list(map(int, input().split())))

    dp = [[0 for _ in range(n+1)] for _ in range(2)]

    for i in range(1, n+1):
        dp[0][i] = max(dp[1][i-1] + score[0][i-1], dp[0][i-1])
        dp[1][i] = max(dp[0][i-1] + score[1][i-1], dp[1][i-1])
    
    print(max(dp[0][n], dp[1][n]))
