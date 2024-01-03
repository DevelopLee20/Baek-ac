import sys
a,b,c = map(int,sys.stdin.readline().split())

print(int((c-a)/(a-b)+1.999999))