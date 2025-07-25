total_cost = int(input())
cost_list = []
for _ in range(9):
    cost_list.append(int(input()))

print(total_cost - sum(cost_list))
