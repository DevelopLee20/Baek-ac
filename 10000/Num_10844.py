'''
dp로 각 단계에서 다음 생성될 개수를 더해서 반복
'''

# 입력
N = int(input())

# 초기값 설정(1~9의 경우의 수는 1가지, 0은 0가지)
dp = [[0 for _ in range(10)] for _ in range(N)]
for idx in range(1, 10):
    dp[0][idx] = 1

# 반복으로 dp 리스트 작성
for n in range(1, N):
    dp[n][0] = dp[n-1][1] % 1000000000

    for num in range(1, 9):
        dp[n][num] = (dp[n-1][num-1] + dp[n-1][num+1]) % 1000000000

    dp[n][9] = dp[n-1][8] % 1000000000

# 최종합계 출력
print(sum(dp[N-1]) % 1000000000)
