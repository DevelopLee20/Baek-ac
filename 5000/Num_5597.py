'''
lst = [0 for _ in range(30)]

for _ in range(28):
    lst[int(input()) - 1] = 1

count = 2

for num, i in enumerate(lst):
    if i != 1 and count:
        print(num+1)
        count = count - 1
'''
import sys

input = sys.stdin.readline

assignList = [i+1 for i in range(30)]
for _ in range(28):
    student = int(input())

    assignList[student-1] = 0

for num in assignList:
    if num != 0:
        print(num)
