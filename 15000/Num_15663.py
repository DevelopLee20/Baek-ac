from itertools import permutations

N, M = map(int, input().split())
N_list = list(map(int, input().split()))

answer = set(permutations(N_list, M))

for i in sorted(answer):
    print(*i)
