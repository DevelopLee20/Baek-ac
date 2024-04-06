'''
1. 평균 출력
2. 중앙값 출력
3. 최빈값 출력
4. 범위

평균 출력은 간단
나머지는 정렬하고나서 하면 될듯
이진분류
'''
import sys

input = sys.stdin.readline

N = int(input())
NList = []

for i in range(N):
    NList.append(int(input()))

print((sum(NList) // N) + (sum(NList) % N != 0))
print(NList[(N // 2)])
