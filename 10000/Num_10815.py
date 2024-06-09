import sys
input = sys.stdin.readline

N = int(input())
NList = {i for i in map(int, input().rstrip().split())}
M = int(input())
MList = [i for i in map(int, input().rstrip().split())]

for m in range(M):
    if MList[m] in NList:
        MList[m] = 1
    else:
        MList[m] = 0

print(*MList)
