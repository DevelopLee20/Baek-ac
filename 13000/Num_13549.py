from collections import deque

N, K = map(int, input().split())

INF = float('inf')
visited = [INF] * (100001)
visited[N] = 0
queue = deque()
queue.append((N, 0))

while queue:
    idx, cnt = queue.popleft()
    
    for n_idx, val in [(idx+1, 1), (idx-1, 1), (2*idx, 0)]:
        # 적으면 갱신 후 queue에 삽입
        if 0 <= n_idx < 100001 and visited[n_idx] > cnt + val:
            visited[n_idx] = cnt + val
            queue.append((n_idx, cnt + val))

print(visited[K])
