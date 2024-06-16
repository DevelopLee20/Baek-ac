'''
DP  다이나믹 프로그래밍
2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
n = 1 : 1가지
n = 2 : 3가지
n = 3 : 3 + 1가지
n = 4 : 12가지 3 * 4?
n = 5 : 12 * 3 ㅇㅋ
'''
N = int(input())
dp = [0] * (N+1)
dp[1] = 1

if N > 1:
    dp[2] = 3

for idx in range(3, N+1):
    dp[idx] = 2 * dp[idx-2] + dp[idx-1]
    dp[idx] = dp[idx] % 10007

print(dp[N])
