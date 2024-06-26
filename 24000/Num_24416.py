def fibonacci(n):
    count = 0
    f = [0] * (n+1)
    f[1] = f[2] = 1

    for i in range(3, n+1):
        count += 1
        f[i] = f[i-1] + f[i-2]
    
    print(f[i], count)

n = int(input())
fibonacci(n)
