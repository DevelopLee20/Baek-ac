N = int(input())

for i in range(N):
    line = " " * (N-i-1)
    for j in range(i+1):
        line += "* "
    print(line[:len(line)])
