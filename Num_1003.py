# 시간초과 : 다른 알고리즘으로 찾아야겠다, 다이나믹??? 나중에 다시 온다.

import sys

input = sys.stdin.readline

def fibonacci(n:int, count:list):
    if n == 0:
        count[n] += 1
        return 0
    elif n == 1:
        count[n] += 1
        return 1
    else:
        return fibonacci(n-1, count) + fibonacci(n-2, count)
    
for _ in range(int(input())):
    count = [0,0]
    fibonacci(int(input()), count)
    print(*count)
