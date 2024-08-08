N, M = map(int, input().split())

if M == 1:
    for idx in range(N):
        print(idx+1)
else:
    NumList = [1 for _ in range(M)]
    
    while N*M != sum(NumList):
        print(*NumList, sep=" ")
        
        NumList[-1] += 1
        for idx in range(M-1, -1, -1):
            if NumList[idx] > N:
                NumList[idx-1] += 1
                
                for idx2 in range(idx, M):
                    NumList[idx2] = NumList[idx-1]

    print(*NumList, sep=" ")
