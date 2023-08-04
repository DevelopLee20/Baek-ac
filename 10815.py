import sys

input = sys.stdin.readline

have_count = int(input())
have_card = [i for i in input().split(' ')]
count = input()
card = [int(i in have_card) for i in input().split(' ')]

for i in card:
    print(i, end=' ')