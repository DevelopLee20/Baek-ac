c = []

for i in range(2,10001):
    rt = True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            rt = False
            break
    if rt:
        c.append(i)

def check(a,c):
    num = 0
    while 1:
        if a//2+num in c and a//2-num in c:
            print(a//2-num,a//2+num) 
            break
        num += 1

for _ in range(int(input())):

    a = int(input())
    check(a,c)