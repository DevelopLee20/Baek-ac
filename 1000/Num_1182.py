import sys

N, S = map(int, sys.stdin.readline().split(" "))
number_list = [int(i) for i in sys.stdin.readline().split(" ")]

count = 0
def dfs(idx: int, value: int):
    global count

    if idx == N:
        if value == S:
            count += 1
    
        return

    dfs(idx+1, value+number_list[idx])
    dfs(idx+1, value)

dfs(0, 0)
if S == 0:
    count -= 1
    
print(count)
