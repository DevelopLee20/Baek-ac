# 64, 32, 16, 8, 4, 2, 1
# 비트의 1값의 합이네..

X = int(input())

X_bit = bin(X)

X_bit = [int(i) for i in X_bit[2:]]
print(sum(X_bit))
