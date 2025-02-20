import sys

n = int(sys.stdin.readline())

drink_list = []
for _ in range(n):
    drink = int(sys.stdin.readline())
    drink_list.append(drink)

dp = [0] * (n+1)
dp[0] = drink_list[0]
if n > 1:
    dp[1] = drink_list[0] + drink_list[1]
if n > 2:
    dp[2] = max(dp[1], drink_list[0] + drink_list[2], drink_list[1] + drink_list[2])

for index in range(3, n):
    not_drink = dp[index-1]
    together_drink = drink_list[index] + drink_list[index-1] + dp[index-3]
    solo_drink = drink_list[index] + dp[index-2]

    dp[index] = max(not_drink, together_drink, solo_drink)

print(dp[n-1])
