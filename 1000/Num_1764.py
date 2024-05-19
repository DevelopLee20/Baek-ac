import sys

input = sys.stdin.readline

N, M = map(int, input().split())

NDic = {}
for _ in range(N):
    name = input().rstrip()
    NDic.sort()

for _ in range(M):
    name = input().rstrip()
