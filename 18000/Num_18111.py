import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

board = {}
BlockSum = B
for _ in range(N):
    for i in [int(i) for i in input().rstrip().split()]:
        BlockSum += i
        if i in board:
            board[i] += 1
        else:
            board[i] = 1

MaxHeight = int(BlockSum / (N*M))
ResultSec = 2 * 256 * N * M + 1; ResultHeight = -1

for TargetHeight in range(0, MaxHeight+1):
    sec = 0
    for height, count in board.items():
        gap = TargetHeight - height

        if gap > 0:
            sec += gap * count
        elif gap < 0:
            sec += gap * count * -2

    if ResultSec > sec:
        ResultHeight = TargetHeight
        ResultSec = sec
    elif ResultSec == sec and ResultHeight < TargetHeight:
        ResultHeight = TargetHeight

print(ResultSec, ResultHeight)
