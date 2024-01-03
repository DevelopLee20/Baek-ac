N, M = map(int, input().split())

def divide(N, M):
    if N + M == 2:
        return 0
    
    if N > M:
        return divide(N//2, M) + divide(N-N//2, M) + 1
    else:
        return divide(N, M//2) + divide(N, M-M//2) + 1

print(divide(N, M))
