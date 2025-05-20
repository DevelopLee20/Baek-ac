num_list = []

for _ in range(7):
    num = int(input())
    
    if num % 2 != 0:    
        num_list.append(num)

if num_list:
    num_sum = sum(num_list)
    num_min = min(num_list)
    print(num_sum)
    print(num_min)
else:
    print(-1)
