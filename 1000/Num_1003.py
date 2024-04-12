'''
나온대로 작성
T 케이스 개수
N -> T개 만큼 출력


출력 -> (0 호출 횟수) (1 호출 횟수)

'''

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    zero = 1; one = 0
    for __ in range(N):
        next = zero + one
        zero = one
        one = next
    
    print(zero, one)
