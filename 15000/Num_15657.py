# 입력
N, M = map(int, input().split())
N_list = [int(i) for i in input().split()]

# 리스트 전처리
pre_N_list = sorted(set(N_list))
# print(pre_N_list) # debug

# dfs로 출력
def dfs(depth: int, index: int, output: list):
    if depth == M:
        print(*output, sep=" ")
        return

    for idx in range(index, N): # 추가된 수보다 낮은 수는 다음에 오지 못하게 제한
        output.append(pre_N_list[idx])
        dfs(depth+1, idx, output)
        output.pop()            # 리스트 초기화

for idx in range(len(pre_N_list)):
    dfs(1, idx, [pre_N_list[idx]])
