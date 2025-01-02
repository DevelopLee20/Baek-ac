import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())

    for val in range((j-i+1) // 2):
        num_list[i-1+val], num_list[j-1-val] = num_list[j-1-val], num_list[i-1+val]

print(*num_list, sep=" ")
