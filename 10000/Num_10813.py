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