'''
<<<<<<< HEAD
1. 평균 출력
2. 중앙값 출력
3. 최빈값 출력
4. 범위

평균 출력은 간단
나머지는 정렬하고나서 하면 될듯
이진분류
'''
=======
리스트를 탐색하는 것보다 딕셔너리를 탐색하는 것이 더 효율적이다.
'''

>>>>>>> 7917cfa20239c9af7d583535b11a535fc567f9ca
import sys

input = sys.stdin.readline

N = int(input())
<<<<<<< HEAD
NList = []

for i in range(N):
    NList.append(int(input()))

print((sum(NList) // N) + (sum(NList) % N != 0))
print(NList[(N // 2)])
=======

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
>>>>>>> 7917cfa20239c9af7d583535b11a535fc567f9ca
