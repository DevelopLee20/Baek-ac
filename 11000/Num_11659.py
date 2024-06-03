import sys

input = sys.stdin.readline

N, M = map(int, input().split())

numList = [0 for i in range(N+1)]
for idx, num in enumerate(input().rstrip().split()):
    numList[idx+1] = numList[idx] + int(num)

for m in range(M):
    i, j = map(int, input().split())

    print(numList[j] - numList[i-1])
