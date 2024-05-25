'''
<그림 1>과 같이 정사각형 모양의 지도가 있다.
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다.
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

3
7
8
9
'''
import sys

input = sys.stdin.readline
N = int(input())

graph = []
for _ in range(N):
    row = [int(i) for i in input().rstrip()]
    graph.append(row)

visited = []
def bfs(x, y):
    queue = [(x, y)]
    count = 0
    visited.append((x, y))

    while len(queue) > 0:
        x, y = queue.pop(0)
        count += 1

        if x > 0 and graph[x-1][y] == 1 and (x-1, y) not in visited:
            queue.append((x-1, y))
            visited.append((x-1, y))
        if x < N-1 and graph[x+1][y] == 1 and (x+1, y) not in visited:
            queue.append((x+1, y))
            visited.append((x+1, y))
        if y > 0 and graph[x][y-1] == 1 and (x, y-1) not in visited:
            queue.append((x, y-1))
            visited.append((x, y-1))
        if y < N-1 and graph[x][y+1] == 1 and (x, y+1) not in visited:
            queue.append((x, y+1))
            visited.append((x, y+1))
    
    return count

countList = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1 and (x, y) not in visited:
            count = bfs(x, y)
            countList.append(count)

print(len(countList))
print(*sorted(countList), sep="\n")
