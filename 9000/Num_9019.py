import sys
from collections import deque

# 표준 입출력 오버라이딩(T 케이스만큼 반복해서 입력받아야 함으로)
input = sys.stdin.readline

# 테스트 개수 입력
T = int(input())

# 테스트 케이스만큼 반복
for _ in range(T):
    # 입력
    d, target_value = map(int, input().split())

    # deque 대신 리스트를 사용하면 시간초과 발생 가능
    queue = deque([(d)])

    # 이전 기록을 저장(메모리 효율)
    visited = [False] * 10000
    operator = [""] * 10000
    parent = [-1] * 10000
    
    # 시작값 방문 처리
    visited[d] = True

    # bfs 알고리즘
    while len(queue) > 0:
        value = queue.popleft()

        # 목표값일 경우 종료
        if value == target_value:
            break

        # D 연산
        new_value = (value * 2) % 10000
        if not visited[new_value]:
            visited[new_value] = True
            operator[new_value] = "D"
            queue.append(new_value)
            parent[new_value] = value

        # S 연산
        new_value = 9999 if value == 0 else value - 1
        if not visited[new_value]:
            visited[new_value] = True
            operator[new_value] = "S"
            queue.append(new_value)
            parent[new_value] = value

        # L 연산
        new_value = (value % 1000) * 10 + (value // 1000)
        if not visited[new_value]:
            visited[new_value] = True
            operator[new_value] = "L"
            queue.append(new_value)
            parent[new_value] = value

        # R 연산
        new_value = (value % 10) * 1000 + int(value / 10)
        if not visited[new_value]:
            visited[new_value] = True
            operator[new_value] = "R"
            queue.append(new_value)
            parent[new_value] = value

    result = []
    current = target_value
    while current != d:
        result.append(operator[current])
        current = parent[current]
    
    print("".join(result[::-1]))
