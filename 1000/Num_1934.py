import sys

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    upper = A * B

    while B != 0:
        r = A % B
        A = B
        B = r
    
    print(int(upper / A))
