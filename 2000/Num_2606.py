'''
링크드 리스트로 구현 2차원.
count 값으로 세서 결과 출력
'''

import sys

input = sys.stdin.readline

num = int(input())
linked_list = [[0 for _ in range(num)] for __ in range(num)]
virus = [0 for _ in range(num)]
check = [0]

for _ in range(int(input())):
    i, j = map(int, input().split(" "))
    linked_list[i-1][j-1] = 1
    linked_list[j-1][i-1] = 1

while len(check):
    start = check.pop()
    if virus[start] == 0:
        virus[start] = 1
        
        for num, i in enumerate(linked_list[start]):
            if i == 1 and virus[num] == 0 and num not in check:
                check.append(num)
                
print(sum(virus)-1)
