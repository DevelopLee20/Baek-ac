graph = [list(map(int, input().split())) for _ in range(4)]

count = 0
max_count = 0
for person_in, person_out in graph:
    count = count - person_in + person_out
    max_count = max(max_count, count)

print(max_count)
