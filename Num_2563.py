import sys

board = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(int(sys.stdin.readline())):
    a, b = map(int,sys.stdin.readline().split())
    for i in range(a-1,a+9):
        for j in range(b-1, b+9):
            board[i][j] = 1
            
print(sum(sum(board, [])))