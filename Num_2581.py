a = int(input())
b = int(input())
sum = 0
get = -1
first = True

for i in range(a,b+1):
    chk = True
    if i == 1:
        chk = False
    for j in range(2,i):
        if i%j == 0:
            chk = False
            break
    if chk:
        sum += i
    if chk and first:
        get = i
        first = False

if get == -1:
    print(-1)
else:
    print(sum)
    print(get)