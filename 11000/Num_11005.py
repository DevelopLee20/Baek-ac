# 입력
N, B = map(int, input().split())

if N == 0:
    print(N)
    exit(0)

# B 진법으로 변환
value = 1
while value * B <= N:
    value *= B

while value > 0:
    quotient = N // value
    N %= value
    if quotient < 10:
        print(quotient, end="")
    else:
        print(chr(quotient+55), end="")
    value //= B
