import sys

input = sys.stdin.readline

siteName = {}
N, M = map(int, input().split())
for _ in range(N):
    name, password = input().rstrip().split()
    siteName[name] = password

for _ in range(M):
    name = input().rstrip()
    print(siteName[name])
