import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
NList = []

for _ in range(N):
    num = int(input())

    NList.append(num)

# 선택정렬
# 0 1 2 3
# 0부터 차례로 비교 후 변경

for i in range(1, N):
    for j in range(i, 0, -1):
        if NList[j] < NList[j-1]:
            NList[j], NList[j-1] = NList[j-1], NList[j]

print((sum(NList) // N) + ((sum(NList) % N) != 0))
print(NList[N // 2])
print(Counter(NList))
print(NList[-1] - NList[0])
