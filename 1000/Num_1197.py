import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력
INF = float('inf')
V, E = map(int, input().split())
vertexes = []
for _ in range(E):
    A, B, C = map(int, input().split())
    
    vertexes.append((A-1, B-1, C)) # start, dest, cost

# 분리 집합 찾기
parent = [i for i in range(V)]
def find_root(x):
    if parent[x] == x:
        return x
    
    parent[x] = find_root(parent[x])
    return parent[x]

def set_root(x, y):
    x = find_root(x)
    y = find_root(y)
    
    if x != y:
        parent[y] = x

# 크루스칼 알고리즘
result_cost = 0
node_cnt = 0
for start, dest, cost in sorted(vertexes, key=lambda x: x[2]):
    if find_root(start) != find_root(dest):
        set_root(start, dest)
        
        x = start
        whil True:
            
        
        result_cost += cost

        if node_cnt == V-1:
            break

# 출력
print(result_cost)
