import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
for k in range(K):
    x, y = map(int, input().split())    
    graph[x-1][y-1] = 2 # 사과는 2

rotate = {}
move = [(0, 1), (-1, 0), (0, -1), (1, 0)]
L = int(input())
for l in range(L):
    tim, rot = input().rstrip().split()
    tim = int(tim)
    
    if rot == 'L':    
        rotate[tim] = 1
    else: # elif rot == 'D':
        rotate[tim] = -1

direction = 0
time = 1
x = 0; y = 0
queue = deque()
queue.append((0, 0))
while 1:
    new_x = x + move[direction][0]
    new_y = y + move[direction][1]
    
    if 0 <= new_x < N and 0 <= new_y < N:
        if graph[new_x][new_y] == 2:
            graph[new_x][new_y] = 0
            queue.append((new_x, new_y))
        elif graph[new_x][new_y] == 0 and (new_x, new_y) not in queue:
            queue.popleft()
            queue.append((new_x, new_y))
        else:
            break
    else:
        break
    
    if time in rotate:
        direction = (direction + rotate[time]) % 4
    
    time += 1
    x = new_x
    y = new_y

print(time)
