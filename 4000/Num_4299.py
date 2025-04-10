import sys

x, y = map(int, input().split())

for i in range(x, x//2-1, -1):
    a = i
    b = x - i

    if a + b == x and abs(a - b) == y:
        print(a, b)
        sys.exit(0)

print(-1)
