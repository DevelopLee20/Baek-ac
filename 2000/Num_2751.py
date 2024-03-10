'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

5
5
4
3
2
1

1
2
3
4
5

sort 함수는 원 배열을 수정
sorted 함수는 원 배열을 수정하지 않는다
'''
import sys

input = sys.stdin.readline

N = int(input())

lst = [int(input()) for i in range(N)]

for i in sorted(lst):
    print(i)
