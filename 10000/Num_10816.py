'''
숫자 카드의 개수 N
숫자 카드의 정수 1 2 3
그 다음 M
숫자 카드의 정수 1 2 3
몇 개 있는지 판단
'''

import sys
from collections import Counter

input = sys.stdin.readline

N = input()
N_num = [i for i in input().rstrip().split(" ")]
M = input()
M_num = [i for i in input().rstrip().split(" ")]

count = Counter(N_num)

for i in M_num:
    if i in count:
        print(count[i], end=" ")
    else:
        print(0, end=" ")
