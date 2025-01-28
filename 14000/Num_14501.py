import sys

N = int(sys.stdin.readline())
T = []
P = []

for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)
for n in range(1, N+1):
    Pmax = dp[n-1]
    for day in range(n):
        if day + T[day] == n:
            Pmax = max(P[day]+dp[day], Pmax)

    dp[n] = Pmax

print(dp[-1])
