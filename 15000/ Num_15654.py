N, M = map(int, input().split())
NList = sorted([int(i) for i in input().split()])

def backtracking(tempList: list, idx: int):
    if idx == M:
        print(*tempList)
        return
    
    for num in NList:
        tempList[idx] = num
        
        if len(tempList[:idx+1]) == len(set(tempList[:idx+1])):
            backtracking(tempList, idx+1)

for num in NList:
    tempList = [num for _ in range(M)]
    backtracking(tempList, 1)
