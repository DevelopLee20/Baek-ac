from collections import deque

N = int(input())

dp = [0] * (N+1)
mulList = [i*i for i in range(1, int(N**0.5 + 1))]
queue = deque([0])

while len(queue):
    state = queue.popleft()

    for mul in mulList:
        if state + mul <= N:
            if dp[state + mul] == 0:
                dp[state + mul] = dp[state] + 1
                queue.append(state + mul)
        else:
            break

print(dp[N])
