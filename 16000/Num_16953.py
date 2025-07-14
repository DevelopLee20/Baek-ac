from collections import deque
import sys

# 입력
A, B = map(int, input().split())

# bfs 알고리즘
def bfs(A, B):
    # A~B 크기의 그래프 생성
    visited = set()
    visited.add(A)
    
    # 시작점 초기화
    queue = deque()
    queue.append((A, 0))
    
    while queue:
        num, cnt = queue.popleft()
        
        for next_num in [num*2, num*10+1]:
            # 유효 범위 and 방문 여부
            if A <= next_num <= B and next_num not in visited:
                # 도착 여부
                if next_num == B:
                    return cnt + 1
                
                # 미도착시 다시 탐색
                visited.add(next_num)
                queue.append((next_num, cnt + 1))
    
    return -2

# 출력
print(bfs(A, B) + 1)
