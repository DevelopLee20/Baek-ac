import sys

for line in sys.stdin:
    n = int(line.strip())

    target = 1
    length = 1
    while (target % n):
        target = target * 10 + 1
        length += 1

    print(length)
