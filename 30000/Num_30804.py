from collections import defaultdict

N = int(input())
fruit_list = [int(i) for i in input().split(" ")]

start = 0
count = 1
fruit_count = defaultdict(int)
for end in range(N):
    fruit_count[fruit_list[end]] += 1

    while len(fruit_count) > 2:
        fruit_count[fruit_list[start]] -= 1
        if fruit_count[fruit_list[start]] == 0:
            del fruit_count[fruit_list[start]]

        start += 1
    
    count = max(count, end - start + 1)

print(count)
