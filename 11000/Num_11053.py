N = int(input())
A = [int(i) for i in input().split(" ")]
bf = [1] * N

for i in range(1, N):
    value = 0
    for j in range(i, -1, -1):
        if A[j] < A[i] and value < bf[j]:
            value = bf[j]
    
    bf[i] += value

print(max(bf))
