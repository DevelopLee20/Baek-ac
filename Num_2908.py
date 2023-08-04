a,b = map(str,input().split())

a = int(a[2])*100+int(a[1])*10+int(a[0])
b = int(b[2])*100+int(b[1])*10+int(b[0])

print(max(a,b))

a,b = map(str,input().split())
print(max(int(a[::-1]),int(b[::-1])))