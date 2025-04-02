# A, B = map(int, input().split())

# lcm = max(A, B)

# while lcm % A or lcm % B:
#     lcm += 1

# print(lcm)

A, B = map(int, input().split())
a, b = sorted([A, B])

while b:
    a, b = b, a % b

print(A * B // a)
