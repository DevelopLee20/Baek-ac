'''
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

조건: 중복 안됨, 순서대로 출력
'''

N, M = map(int, input().split())

def backtracking(tempList: list, idx: int):
    if idx == M:
        print(*tempList)
        return
        
    for num in range(1, N+1):
        tempList[idx] = num

        if len(tempList[:idx+1]) == len(set(tempList[:idx+1])): # 중복확인
            backtracking(tempList, idx+1)
    
    return

for num in range(1, N+1):
    tempList = [0 for i in range(M)]
    tempList[0] = num
    backtracking(tempList, 1)
