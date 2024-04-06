import sys

input = sys.stdin.readline

for _ in range(3):
    result = 0

    for count in range(int(input())):
        result += int(input())

    if result > 0:
        print("+")
    elif result < 0:
        print("-")
    else:
        print(0)
