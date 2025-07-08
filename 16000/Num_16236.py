import sys
from collections import deque

# 입력
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def start_shark():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                x = i    # 시작 x 좌표
                y = j    # 시작 y 좌표
                graph[i][j] = 0
                return x, y

x, y = start_shark()

# 초기 상어 크기[크기, 먹은 물고기 수]
shark_size = [2, 0]

# 위, 왼쪽, 오른쪽, 아래
delta_xy = [(-1, 0), (0, -1), (0, 1), (1, 0)]
def find_fish(x: int, y: int):
    queue = deque()
    queue.append((x, y, 0))
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    fishes = []
    
    while queue:
        x, y, count = queue.popleft()   # x, y, 이동한 시간(초)
        
        for dx, dy in delta_xy:
            new_x = x + dx  # 다음 x 좌표
            new_y = y + dy  # 다음 y 좌표
            
            # 좌표가 유효하고 방문하지 않았는지 검사
            if 0 <= new_x < N and 0 <= new_y < N and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                if 0 < graph[new_x][new_y] < shark_size[0]:     # 상어 크기가 크면 먹기
                    fishes.append((new_x, new_y, count+1))      # 먹을 수 있는 물고기 기록
                
                if graph[new_x][new_y] <= shark_size[0]:    # 못먹고 이동 가능하면 이동
                    queue.append((new_x, new_y, count+1))

    if fishes:  # 먹을 수 있는 물고기가 있으면
        return sorted(fishes, key=lambda x: (x[2], x[0], x[1]))[0]
    return (-1, -1, -1) # 이동 불가

count = 0
while True:
    x, y, cnt = find_fish(x, y) # 초기 좌표에서 물고기 찾기 실행
    
    if x == y == -1:    # 못찾았으면 종료
        break
    
    graph[x][y] = 0     # 먹었음으로 빈 칸으로 변경
    count += cnt        # 이동한 시간(초) 추가
    shark_size[1] += 1  # 상어가 먹었음을 표시
    
    if shark_size[0] == shark_size[1]:  # 크기만큼 먹으면
        shark_size[0] += 1              # 크기 성장
        shark_size[1] = 0               # 먹은 물고기 초기화

print(count)     # 최종 이동한 시간(초) 출력
