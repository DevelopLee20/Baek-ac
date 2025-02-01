N = int(input())

a = 1; b = 1
for _ in range(N-2):
    swap = a + b
    a = b
    b = swap

print(b)
