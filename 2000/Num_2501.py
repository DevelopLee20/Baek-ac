N, K = map(int, input().split())

count = 0
for i in range(1, N+1):
    if N % i == 0:
        count += 1

        if count == K:
            print(i)
            exit(0)

print(0)