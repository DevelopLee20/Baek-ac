import sys

input = sys.stdin.readline

def solution():
    A, B = map(int, input().split())
    
    for i in range(2, min(A, B)+1):
        if not ((A/i)%1 or (B/i)%1):
            return A*B//i

    return A*B

for _ in range(int(input())):
    print(solution())
