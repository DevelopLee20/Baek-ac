# 운동, 휴식, 휴식(최소), 운동 못하면 -1
N, m, M, T, R = map(int, input().split())

now = m
minTime = 0

if M - m < T:
    print(-1)

else:
    while N > 0:
        if now + T <= M:
            now += T
            N -= 1
        else:
            now -= R
            now = max(now, m)
        
        minTime += 1
        
    print(minTime)
