'''
n: 의견의 개수
(절사한 의견의 평균)
절사기준: 위아래로 15%

입력값
의견 개수 n: int
의견 NList: list

절사기준 계산 cut = round(n / 100 * 15)
NList 정렬
result = round(average(NList[cut:n-cut+1]))
print(result)
'''
import sys

input = sys.stdin.readline
n = int(input())

if n == 0:
    print(0)
else:
    NList = []

    for _ in range(n):
        NList.append(int(input()))

    NList.sort()

    cut = int(n / 100 * 15 + 0.5)

    NList = NList[cut: n-cut]
    result = int(sum(NList) / len(NList) + 0.5)

    print(result)

NList = [1,2,3,4,5]
