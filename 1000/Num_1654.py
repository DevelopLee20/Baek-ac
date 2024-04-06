'''
N개의 같은 길이의 랜선이 필요하다.
K개의 길이가 다른 랜선이 있다.
랜선을 자를 수 있는데, 붙일수는 없다.

K -> N
A
B
C
D

11개를 만들었을 때, 랜선길이 최대값

sum(랜선길이) / N = 최대값
최대값에서 나머지 랜선의 길이를 고려해야 함

A // x = A1
B // x = B1
C // x = C1
D // x = D1

A1+B1+C1+D1 = 11개?
적다면 x를 얼마나 줄이기? 일단 하나
x의 시작점은? sum(랜선길이) / N = 최대값

배운점: 범위가 정해져있을 경우 브루트포스보다 이진탐색이 효과적이다.
'''
import sys

input = sys.stdin.readline

lanList = []
K, N = map(int, input().split())

for _ in range(K):
    lanList.append(int(input()))

left = 1
right = sum(lanList) // N
result = 0
# lanCount = sum([i//lanMax for i in lanList])

while left <= right:
    mid = (left + right) // 2
    count = sum([i//mid for i in lanList])

    if count >= N:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result, end="")
