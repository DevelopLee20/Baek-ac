import sys

input = sys.stdin.readline

saveList = [0 for _ in range(2**32)]
N = int(input())
for _ in range(N):
    start, end = map(int, input().split())
    