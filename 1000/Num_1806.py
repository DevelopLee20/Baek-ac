from collections import deque

# 우선순위: S를 넘은 것, 길이가 짧은 것, 합이 큰 것(0 으로 처리), 길이가 짧은 것
N, S = map(int, input().split())
num_list = [int(i) for i in input().split()]

start_idx = 0
end_idx = 0
num_sum = 0
min_length = float('inf')
while end_idx < N:
    if num_sum < S:
        num_sum += num_list[end_idx]
        end_idx += 1
        
    if num_sum >= S:
        while num_sum >= S:
            num_sum -= num_list[start_idx]
            start_idx += 1
        
        min_length = min(min_length, end_idx - start_idx + 1)

print(min_length if min_length != float('inf') else 0)
