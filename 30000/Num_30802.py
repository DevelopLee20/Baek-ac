'''
티셔츠 한장, 펜 하나
티셔츠는 같은 사이즈 T장 묶음으로 주문 가능
펜은 P자루씩 묶음으로 주문 or 1자루씩 주문


티셔츠 [S, M, L, XL, XXL, XXXL] 6 종류
펜 P 자루

입력
참가자 수
티셔츠 필요 개수 리스트
티셔츠 묶음 수, 펜의 묶음 수

출력
티셔츠 주문하는 묶음
펜 주문 묶음, 단품
'''
import sys
input = sys.stdin.readline

N = int(input())
TList = [i for i in map(int, input().split())]
T, P = map(int, input().split())

print(sum([int(i/T) + (int(i/T) != i/T) for i in TList]))
print(int(N / P), N % P)
