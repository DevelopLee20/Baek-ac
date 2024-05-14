'''
유저 N: edge 개수
친구 관계 M: node 개수
모두 연결되어 있다.
모두 연결하는데, 짧은 연결만 허용
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0 for i in range(N)] for i in range(N)]
for _ in range(N):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1 # idx라서 -1 해준다.

for i in range(N):
    