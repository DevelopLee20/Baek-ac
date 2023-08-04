'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
10
5
2
3
1
4
2
3
5
1
7
'''

import sys

input = sys.stdin.readline
numList = []

numList.sort()

for i in numList:
    print(i)
