# 1. 입력
S = input()

# 2. 모든 접미사 구하기
S_list = []
for idx in range(len(S)):
    S_list.append(S[idx:])

# 2-debug
# print(S_list)

# 3. 접미사 사전순 정렬 후 출력
for s in sorted(S_list):
    print(s)
