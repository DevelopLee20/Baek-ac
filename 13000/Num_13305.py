# 입력
N = int(input())
length_list = [int(i) for i in input().split()]
cost_list = [int(i) for i in input().split()]

# 초깃값 설정
min_cost = cost_list[0]
total_cost = min_cost * length_list[0]

# 최솟값 찾기
for index in range(1, N-1):
    min_cost = min(min_cost, cost_list[index])
    total_cost += min_cost * length_list[index]

# 출력
print(total_cost)
