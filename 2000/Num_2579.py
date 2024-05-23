import sys

input = sys.stdin.readline

stairCount = int(input())

stairList = []
for idx in range(stairCount):
    score = int(input())
    stairList.append(score)

if stairCount == 1:
    print(stairList[0])
else:
    dp = [0 for _ in range(stairCount)]
    dp[0] = stairList[0]
    dp[1] = stairList[0] + stairList[1]

    if stairCount > 2:
        dp[2] = max(stairList[0] + stairList[2], stairList[1] + stairList[2])

    for i in range(3, stairCount):
        dp[i] = max(dp[i-2] + stairList[i], dp[i-3] + stairList[i-1] + stairList[i])
    
    print(dp[-1])
