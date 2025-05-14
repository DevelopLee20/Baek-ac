import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    input_str = list(map(int, input().split()))

    if input_str[0] == 0:
        break
    
    k = input_str[0]
    S = input_str[1:]

    for comb in combinations(S, 6):
        print(*comb)

    print()
