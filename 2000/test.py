import sys

input = sys.stdin.readline

# 입력 처리
stairCount = int(input())
stairScores = [0] * stairCount
for i in range(stairCount):
    stairScores[i] = int(input())

# 동적 계획법을 위한 배열 초기화
if stairCount == 1:
    print(stairScores[0])
else:
    dp = [0] * stairCount
    dp[0] = stairScores[0]
    dp[1] = stairScores[0] + stairScores[1]

    if stairCount > 2:
        dp[2] = max(stairScores[0] + stairScores[2], stairScores[1] + stairScores[2])

    # DP 테이블 채우기
    for i in range(3, stairCount):
        dp[i] = max(dp[i-2] + stairScores[i], dp[i-3] + stairScores[i-1] + stairScores[i])

    # 최종 결과 출력
    print(dp[-1])
