N = int(input())
Nsum = 1

for i in range(2, N+1):
    Nsum *= i

NsumList = list(str(Nsum))
NsumList.reverse()

count = 0
for i in NsumList:
    if i != '0':
        print(count)
        break
    count += 1
