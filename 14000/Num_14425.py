import sys

input = sys.stdin.readline

N, M = map(int, input().split())
N_list = []
for _ in range(N):
    n = input()
    N_list.append(n)

count = 0
for _ in range(M):
    m = input()
    if m in N_list:
        count += 1

print(count)
