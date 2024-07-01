import sys

input = sys.stdin.readline

N, M = map(int, input().split())
baguni = [i for i in range(1, N+1)]

for m in range(M):
    i, j = map(int, input().split())

    mid = (i + j) / 2
    while i <= mid: