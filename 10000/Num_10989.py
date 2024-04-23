'''
때로는 정렬보다 그냥 리스트에 때려박는게(정확한 범위를 알고 있을 때)가 좋다.
'''
import sys

input = sys.stdin.readline

N = int(input())
NumList = [0] * 10001

for i in range(N):
    num = int(input())
    NumList[num] += 1

for num, count in enumerate(NumList):
    for i in range(count):
        print(num)
