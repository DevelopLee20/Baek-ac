'''
시간초과 원인 : queue 구조 문제
'''

import sys

input = sys.stdin.readline

N = int(input())

queue = [i for i in range(1, N+1)]

for _ in range(N-1):
    queue.pop(0)
    value = queue.pop(0)
    queue.append(value)

print(*queue)
