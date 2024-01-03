import sys

input = sys.stdin.readline
N, M = map(int, input().split(" "))

lst = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split(" "))
    
    for p in range(i-1, j-(i-1) // 2):
        temp = lst[p]
        lst[p] = lst[p+1]
        lst[p+1] = temp
        print("swap", lst[p+1], end=" ")
        print("swap", lst[p])

print(*lst)
