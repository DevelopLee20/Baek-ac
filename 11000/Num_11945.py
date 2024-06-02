import sys
input = sys.stdin.readline

N, M = map(int, input().split())
shape = []
for n in range(N):
    m = [i for i in input().strip()]
    shape.append(m)

for n in range(N):
    for m in range(M-1, -1, -1):
        print(shape[n][m], end="")
    print()
