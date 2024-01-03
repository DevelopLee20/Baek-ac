x, y = map(int, input().split(" "))

bod_1 = [['B','W']*4, ['W','B']*4]*4
bod_2 = [['W','B']*4, ['B','W']*4]*4
board = []
for _ in range(x):
    board.append([i for i in input()])

list_name = []
for start_x in range(x-7):
    for start_y in range(y-7):
        num = 0
        board_check = bod_1
        for i in range(start_x, start_x+8):
            for j in range(start_y, start_y+8):
                if board[i][j] != board_check[i-start_x][j-start_y]:
                    num = num + 1
        list_name.append(num)
        
        num = 0
        board_check = bod_2
        for i in range(start_x, start_x+8):
            for j in range(start_y, start_y+8):
                if board[i][j] != board_check[i-start_x][j-start_y]:
                    num = num + 1
        list_name.append(num)
        
print(min(list_name))