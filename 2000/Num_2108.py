'''
리스트를 탐색하는 것보다 딕셔너리를 탐색하는 것이 더 효율적이다.
'''

import sys

input = sys.stdin.readline

N = int(input())

SList = []
count = {}
SListSum = 0
for _ in range(N):
    num = int(input())
    SListSum += num
    SList.append(num)

    if num in count:
        count[num] += 1
    else:
        count[num] = 0
    

SList.sort()

FNumList = []
countMax = max(count.values())
for key, value in count.items():
    if value == countMax:
        FNumList.append(key)

print(round(SListSum / N))
print(SList[N // 2])

if len(FNumList) == 1:
    print(FNumList[0])
else:
    print(sorted(FNumList)[1])

print(SList[-1] - SList[0])
