import sys

N, K = map(int, sys.stdin.readline().split())

goods_list = []
for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    goods_list.append((weight, value))

value_list = [0] * (K+1)
for weight, value in sorted(goods_list, key=lambda x: x[0], reverse=True):

    for w in range(K, weight-1, -1):
        if value_list[w] != 0 and w + weight <= K:
            value_list[w + weight] = max(value_list[w] + value, value_list[w + weight])
    
    if weight <= K:
        value_list[weight] = max(value_list[weight], value)

# print(value_list)
print(max(value_list))
