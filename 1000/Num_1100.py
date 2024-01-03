board = []

for _ in range(8):
    board.append([i for i in input()])
    
seed = 0
count = 0

for i in board:
    for j in range(4):
        if i[seed + 2*j] == 'F':
            count += 1
    seed += 1
    seed %= 2

print(count)
