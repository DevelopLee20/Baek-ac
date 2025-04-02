# 입력
A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

# 최대공약수 알고리즘, 유클리드 호제법
def gcd(a: int, b: int) -> int:
    a, b = sorted([a, b])
    while b:
        a, b = b, a % b

    return a

lower = B1 * B2 // gcd(B1, B2)                  # 분모
upper = A1 * (lower // B1) + A2 * (lower // B2) # 분자

# 약분
common = gcd(lower, upper)

# 출력
print(upper // common, lower // common)
