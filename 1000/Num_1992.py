import sys

N = int(sys.stdin.readline())
graph = [[i for i in sys.stdin.readline().strip()] for _ in range(N)]

def is_same(x1: int, x2: int, y1: int, y2: int) -> bool:
    for x in range(x1, x2):
        for y in range(y1, y2):
            if graph[x][y] != graph[x1][y1]:
                return False
    
    return True

def divide(x1: int, x2: int, y1: int, y2: int) -> str:
    if is_same(x1, x2, y1, y2):
        return graph[x1][y1]
    else:
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        
        v1 = divide(x1, mid_x, y1, mid_y)
        v2 = divide(x1, mid_x, mid_y, y2)
        v3 = divide(mid_x, x2, y1, mid_y)
        v4 = divide(mid_x, x2, mid_y, y2)
        
        return "(" + v1 + v2 + v3 + v4 + ")"

print(divide(0, N, 0, N))
