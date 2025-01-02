N = int(input())

num = 2
for _ in range(N):
    num += (num - 1)

result = num**2
print(result)
