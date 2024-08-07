N, M = map(int, input().split())

NBin = [1 for _ in range(N)]

if N == 1:
    print(1)
elif M == 1:
    for idx in range(N):
        print(idx+1)
else:
    while sum(NBin) > 0:
        if sum(NBin) == M:
            output = []
            for num, n in enumerate(NBin):
                if n:
                    output.append(num+1)
            
            print(*output, sep=" ")
            
        NBin[-1] -= 1
    
        for idx in range(N-1, 0, -1):
            if NBin[idx] == -1:
                NBin[idx-1] -= 1
                NBin[idx] = 1
            else:
                break
