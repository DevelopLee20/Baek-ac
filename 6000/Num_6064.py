import sys
input = sys.stdin.readline

def LCM(a: int, b: int):
    while a % b != 0:
        r = a % b
        a = b
        b = r
    return b

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    if M+x < N+y:
        M, N = N, M
        x, y = y, x
    
    lcm = (M * N) // LCM(M, N)

    num = x - 1; notNum = True
    while num < lcm:
        x1 = num % M + 1
        y1 = num % N + 1

        if x1 == x and y1 == y:
            notNum = False
            break
        
        num += M
    
    if notNum:
        print(-1)
    else:
        print(num+1)
