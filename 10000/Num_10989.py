import sys

input = sys.stdin.readline

num = int(input())
lst = [0 for i in range(num)]

for i in range(num):
    lst[i] = int(input())

for _ in range(num-1):
    for i in range(num-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            
print(*lst, sep="\n")
