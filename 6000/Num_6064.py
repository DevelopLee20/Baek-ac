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

    ableList = []
    able = (M+x)
    while able <= lcm:
        ableList.append(able)
        able += M

    minusOutput = True
    output = (N+y)
    while output <= lcm:
        if output in ableList:
            minusOutput = False
            break
        output += N
    
    if minusOutput:
        print(-1)
    else:
        print(output)
