A, B, C = map(int, input().split())
# print(pow(A, B, C)) 정답

def divide(A: int, B: int) -> int:
    if B == 0:
        return 1
    half = divide(A, B//2)
    if B % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * A) % C
    
print(divide(A, B))
