import sys

input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

count = {-1: 0, 0: 0, 1: 0}

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def checker(p1: Pos, p2: Pos) -> bool:
    pattern = graph[p1.x][p1.y]

    for i in range(p1.x, p2.x):
        for j in range(p1.y, p2.y):
            if pattern != graph[i][j]:
                return False

    return True

def divide(p1: Pos, p2: Pos):
    global count

    if checker(p1, p2):
        count[graph[p1.x][p1.y]] += 1
        return

    size = (p2.x - p1.x) // 3
    for i in range(3):
        for j in range(3):
            next_p1 = Pos(p1.x + i * size, p1.y + j * size)
            next_p2 = Pos(next_p1.x + size, next_p1.y + size)
            divide(next_p1, next_p2)

divide(Pos(0, 0), Pos(N, N))

for i in [-1, 0, 1]:
    print(count[i])
