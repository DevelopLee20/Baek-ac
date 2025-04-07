N = int(input())

count = 0
visited_col = [False] * N
visited_cross_1 = [False] * (2*N-1)
visited_cross_2 = [False] * (2*N-1)
def backtracking(row: int) -> None:
    global count
    if row == N: # 체스판 끝(end of row)에 도착
        count += 1
        return
    
    # 다음 행 중 가능한 것만 진행
    for col in range(N):
        cross1 = N - 1 + row - col
        cross2 = row + col

        if not (visited_col[col] or visited_cross_1[cross1] or visited_cross_2[cross2]):
            visited_col[col] = True
            visited_cross_1[cross1] = True
            visited_cross_2[cross2] = True

            backtracking(row+1)

            visited_col[col] = False
            visited_cross_1[cross1] = False
            visited_cross_2[cross2] = False
    return

backtracking(0) # 현재 위치 퀸 두기

print(count)
