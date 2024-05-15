'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
lst = [i for i in range(1, N+1)]

for _ in range(M):
    idx1, idx2 = map(int ,input().split(" "))
    temp = lst[idx1 - 1]
    lst[idx1 - 1] = lst[idx2 - 1]
    lst[idx2 - 1] = temp

print(*lst)
'''

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

basket = [i+1 for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)
