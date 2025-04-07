import sys
from math import gcd
from functools import reduce

# 입력
N = int(sys.stdin.readline())
N_list = []
for _ in range(N):
    N_list.append(int(sys.stdin.readline()))

# 간격 계산
N_gap_list = [0] * N
for idx in range(N-1):
    N_gap_list[idx] = N_list[idx+1] - N_list[idx]

# 최대공약수 계산
gap = reduce(gcd, N_gap_list)
# print("gcd", gcd) # debug

# 출력
print((N_list[-1] - N_list[0])//gap + 1 - N)
