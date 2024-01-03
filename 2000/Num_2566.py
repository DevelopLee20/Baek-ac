field = [[int(i) for i in input().split(" ")] for _ in range(9)]
x = 0
y = 0
mvalue = -1

for i in range(9):
    for j in range(9):
        if field[i][j] > mvalue:
            mvalue = field[i][j]
            x = i
            y = j

print(mvalue)
print(x+1, y+1)
