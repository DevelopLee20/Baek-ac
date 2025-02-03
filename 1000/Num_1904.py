N = int(input())

fib1 = 1
fib2 = 1

for i in range(N-1):
    swap = (fib1 + fib2) % 15746
    fib1 = fib2
    fib2 = swap

print(fib2)
