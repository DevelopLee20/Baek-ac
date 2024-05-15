'''
N, M = map(int, input().split(" "))
lst = [0 for _ in range(N)]
for _ in range(M):
    i, j, k = map(int, input().split(" "))
    
    for i in range(i-1, j):
        lst[i] = k

print(*lst)
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

backet = [0 for _ in range(N)]
for _ in range(M):
    i, j, k = map(int, input().split())

    for num in range(i, j+1):
        backet[num-1] = k

print(*backet, sep=" ")
