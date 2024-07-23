'''
1달러 = 100센트
25센트
10센트
05센트
01센트

입력은 센트
123
'''
import sys

input = sys.stdin.readline

T = int(input())
for t in range(T):
    C = int(input())
    quarter = C // 25
    C = C % 25

    dime = C // 10
    C = C % 10

    nickel = C // 5
    C = C % 5
        
    penny = C

    print(quarter, dime, nickel, penny)
