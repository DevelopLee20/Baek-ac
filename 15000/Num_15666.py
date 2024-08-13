N, M = map(int, input().split())
NList = sorted(set([int(i) for i in input().split()]))

def backtracking(tempList: list, idx: int):
    if idx == M:
        print(*tempList)
        return
    
    for num in NList:
        if tempList[idx-1] <= num:
            tempList[idx] = num
            backtracking(tempList, idx+1)
    
    return

for num in NList:
    tempList = [0 for _ in range(M)]
    tempList[0] = num

    backtracking(tempList, 1)
