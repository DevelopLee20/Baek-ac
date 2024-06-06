'''
개수를 가진 튜플
받은 리스트
삭제 말고 front end 변수 사용해서
end 전까지 출력함
아니면 deque를 써볼까?
개수가 하나씩 줄어서
앞 몇 개 지울래
뒤 몇 개 지울래
'''
import sys
input = sys.stdin.readline

N = int(input())
NList = [n for n in map(int, input().split())]

freq = {}
for n in NList:
    if 