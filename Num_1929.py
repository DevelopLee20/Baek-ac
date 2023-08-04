# 성공
a,b = map(int,input().split())

if a == 1:
    a += 1
for i in range(a,b+1):
    prime = True
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            prime = False
            break
    if prime:
        print(i)

# 시간 초과
import sys
a,b = map(int,sys.stdin.readline().split())
c = []

if a == 1:
    a += 1

c = [x for x in range(a,b+1)]

for i in c:
    for j in range(2,b+1,i):
        if i*j in c:
            c.remove(i*j)

print(*c,sep='\n')