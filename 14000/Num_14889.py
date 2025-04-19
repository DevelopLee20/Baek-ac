import sys
from itertools import combinations

input = sys.stdin.readline

# N 입력
N = int(input())

# 선수 능력치 입력
graph = []
for _ in range(N):
    row = [int(i) for i in input().split()]
    graph.append(row)

# combinations 함수로 팀 편성
team_comb = list(combinations(range(N), N//2))

# 출력할 최소 차이
min_score = 2001

# 팀에 맞게 점수 계산
for teamA in team_comb[:len(team_comb) // 2]:
    teamA = set(teamA)
    scoreA = 0; scoreB = 0
    for i in range(N):
        isA = False
        if i in teamA:
            isA = True

        for j in range(i+1, N):
            if isA and j in teamA:
                scoreA += graph[i][j] + graph[j][i]
            elif not isA and j not in teamA:
                scoreB += graph[i][j] + graph[j][i]

    min_score = min(min_score, abs(scoreA - scoreB))

print(min_score)
