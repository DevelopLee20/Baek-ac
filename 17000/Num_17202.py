'''
16자리 -> 15자리 -> 14자리 -> ... -> 2자리(종료)
0, 1 사용 후 0에 저장
'''

A = input()
B = input()

dp = []
for a, b in zip(A, B):
    dp.append(int(a))
    dp.append(int(b))

for end in range(15, 1, -1):
    for idx in range(0, end):
        dp[idx] = (dp[idx] + dp[idx+1]) % 10

if dp[0] == 0:
    print(f'0{dp[1]}')
else:
    print(f'{dp[0]}{dp[1]}')
