N, r, c = map(int, input().split())

x1 = 0
y1 = 0
x2 = 2**N
y2 = 2**N
output = 0

for i in range(N-1, -1, -1):
    valueX = (x2+x1) // 2
    valueY = (y2+y1) // 2

    if r < valueX and c < valueY:
        x2 = valueX
        y2 = valueY
    elif r < valueX and c >= valueY:
        output += 4**i
        x2 = valueX
        y1 = valueY
    elif r >= valueX and c >= valueY:
        output += (4**i) * 3
        x1 = valueX
        y1 = valueY
    else: # x >= valueX and y < valueY
        output += (4**i) * 2
        x1 = valueX
        y2 = valueY

print(output)
