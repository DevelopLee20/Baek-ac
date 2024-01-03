import sys

for _ in range(int(sys.stdin.readline())):
    b = input()
    stack = 0; score = 0

    for j in b:
        if j == 'O':
            score = score + 1 + stack
            stack += 1
        else:
            stack = 0
    print(score)