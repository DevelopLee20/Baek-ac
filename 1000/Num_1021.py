from collections import deque

# 입력
N, M = map(int, input().split())
M_list = [int(i) for i in input().split()]

# 덱으로 생성
queue = deque([int(i) for i in range(1, N+1)])
count = 0

# 타겟마다 반복
for m in M_list:
    # 타겟의 위치 검색
    target = queue.index(m)

    # 타겟의 위치가 전체크기의 절반에서 왼쪽인지 오른쪽인지 판단, 적은 수의 rotate 진행
    if target <= len(queue) // 2:
        queue.rotate(-target)
        count += target
    else:
        queue.rotate(len(queue) - target)
        count += (len(queue) - target)
    
    # 타겟 제거
    queue.popleft()

# 결과 출력
print(count)
