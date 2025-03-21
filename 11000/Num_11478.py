'''
- 중복 처리는 visited list를 통해 처리
- 이미 방문했다면 되돌아감
- 시작점부터 끝까지 모든 과정을 출력
- 백트래킹으로 모든 과정을 진행
런타임 에러 (RecursionError)
'''

# # 입력
# S = input()

# # 초깃값 설정
# visited = []

# # 백트래킹 함수
# def backtracking(index: int, track: str):
#     if index == len(S):
#         return
    
#     track += S[index]
#     if track not in visited:
#         visited.append(track)  # 방문처리

#     backtracking(index+1, track)    

# # 백트래킹 실행
# for idx in range(len(S)):
#     backtracking(idx, "")

# # 출력
# print(len(visited))

'''
- 위의 아이디어는 동일하되, 역방향으로 생각하기
- 전체 문자열에서 앞 또는 뒤에서 값을 하나씩 제거하면서 진행, 분명하게 종료될 것이라 예상
'''

# # 입력
# S = input()

# # 초깃값 설정
# visited = []

# # 백트래킹 함수
# def backtracking(track: str):
#     if len(track) == 0:
#         return

#     if track not in visited:
#         visited.append(track)
    
#     backtracking(track[1:])
#     backtracking(track[:-1])

# # 백트래킹 실행
# backtracking(S)

# # 출력
# print(len(visited))

'''
- 집합을 사용해 그냥 for 문을 돌리면 된다고 함
'''

S = input()

# 초깃값 설정
visited = set()

for start in range(len(S)):
    for end in range(start+1, len(S)+1):
        visited.add(S[start:end])

print(len(visited))
