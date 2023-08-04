def d(n):
    a = 0
    for x in list(str(n)):
        a = a + int(x) 
    return int(n) + a
a = []; b = []
for i in range(1,10001):
    k = d(i)
    b.append(i)
    a.append(k)
    
k = sorted(set(b)-set(a))
print(*k,sep="\n")