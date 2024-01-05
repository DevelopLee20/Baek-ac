N = int(input())
A = [int(i) for i in input().split(" ")]
B = [int(i) for i in input().split(" ")]

A.sort(reverse=False)
B.sort(reverse=True)

output = 0

for i, j in zip(A, B):
    output += i * j

print(output)
