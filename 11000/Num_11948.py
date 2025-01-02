import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
E = int(sys.stdin.readline())
F = int(sys.stdin.readline())

result = sum(sorted([A, B, C, D])[1:]) + max(E, F)
print(result)
