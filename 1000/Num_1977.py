M = int(input())
N = int(input())

complete_mul_list = []
for i in range(M, N+1):
    if i**0.5 == int(i**0.5):
        complete_mul_list.append(i)

if complete_mul_list:
    print(sum(complete_mul_list))
    print(min(complete_mul_list))
else:
    print(-1)
