'''
지구 E, 태양 S, 달 M
1 <= E <= 15
1 <= S <= 28
1 <= M <= 19

N년 -> ((N % 16) + 1) ((N % 28) + 1) ((N % 19) + 1)
N을 알아내자

(1 + E * 15) (1 + S * 28) (1 + M * 19)
'''

E, S, M = map(int, input().split())
e = s = m = 1
n = 0

while E != e or S != s or M != m:
    n += 1
    e = n % 15 + 1
    s = n % 28 + 1
    m = n % 19 + 1

print(n + 1)
