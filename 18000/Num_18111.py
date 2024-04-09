'''
N: 집터의 세로
M: 집터의 가로
B: 초기 블록 개수

땅의 높이 0~256
최소 시간을 가지는 것이 답이 여러 개라면 땅의 높이가 가장 높은 것

행동1: 블록 제거해서 인벤토리 넣기 -> 2초
행동2: 블록 꺼내서 놓기 -> 1초

입력
N, M, B
board
'''
import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

board = []
for _ in range(N):
    board.append([int(i) for i in input().rstrip().split()])

