'''
N = 1
0, 1
2, 3
1씩 증가

N = 2
0 4
8 12
4씩 증가

N = 3
0 16
32 48
16씩 증가

기준점(왼쪽 맨위) 잡아주고, N으로 기준점 또 잡아주고 최종 1까지 확인하면 종료

증가량 설정 수식: 2**0 2**2 2**4
4**0 4**1 4**2 -> 4**(N-1) 이게 증가 기준 -> 하나씩 위치에 따라서 하나씩 줄여나가기
위치? 현재 기준 두 점 (0,0) (2**N, 2**N)에서 절반인데 절반치선까지는 인정

N = 2
r = 3
c = 1
'''

N, r, c = map(int, input().split())
output = 0

midX = 2**N // 2; midY = 2**N // 2

for i in range(1, N+1):
    if r < midX and c < midY:
        midX //= 2**(N-1) // (2 * i)
        midY //= 2**(N-1) // (2 * i)
    elif r < midX and c >= midY:
        midX //= 2**(N-1) // (2 * i)
        midY += 2**(N-1) // (2 * i)
        output += 4**(N-i)
    elif r >= midX and c < midY:
        midX += 2**(N-1) // (2 * i)
        midY //= 2**(N-1) // (2 * i)
        output += 4**(N-i) * 2
    else:
        midX += 2**(N-1) // (2 * i)
        midY += 2**(N-1) // (2 * i)
        output += 4**(N-i) * 3

print(output)
