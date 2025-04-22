import sys

# 표준입출력 방식 변경
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
graph = [[int(i) for i in input().split()] for _ in range(N)]

# 구간 합 방식으로 계산
prefix = [[0] * (N+1) for _ in range(N+1)]
for row in range(1, N+1):
    for col in range(1, N+1):
        # 왼쪽과 위 값을 더한 후 중복된 부분을 빼기
        prefix[row][col] = graph[row-1][col-1] + prefix[row-1][col] + prefix[row][col-1] - prefix[row-1][col-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]
    print(result)
