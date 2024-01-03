'''
문자는 아스키코드로 변환
abs(abs(ord(현재) - ord(다음)) - abs(현재2 - 다음2)) == 1 일떄만 조건에 성립하는 이동이다.
'''

import sys

move_list = []

for i in range(36):
    move = input()
    move_list.append(move)

def solution():    
    for i in range(1, 36):
        val1 = move_list[i-1]
        val2 = move_list[i]
        val_one = abs(ord(move_list[i-1][0]) - ord(move_list[i][0]))
        val_two = abs(int(move_list[i-1][1]) - int(move_list[i][1]))
        
        if abs(val_one - val_two) != 1:
            return "Invalid"
        
    return "Valid"

print(solution())
