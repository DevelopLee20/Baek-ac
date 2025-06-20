N, M = map(int, input().split())
N_list = list(map(int, input().split()))

count = 0   # 출력할 갯수
value = 0   # 현재 합
tail = 0    # 끝 인덱스
for n in N_list:
    value += n
    
    while value > M:
        value -= N_list[tail]
        tail += 1

    if value == M:
        count += 1

print(count)
